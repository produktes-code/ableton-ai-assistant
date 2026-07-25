import pytest
import socket
import threading
import json
import time
import queue
from concurrent.futures import ThreadPoolExecutor

MOCK_TOKEN = "test_token_12345678"

class MockAntigravityServer:
    def __init__(self, port=0):
        self.port = port
        self.token = MOCK_TOKEN
        self._sock = None
        self._thread = None
        self._running = False
        self.received_commands = []
        self.responses = {}

    def start(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind(('127.0.0.1', self.port))
        self.port = self._sock.getsockname()[1]
        self._sock.listen(5)
        self._sock.settimeout(1.0)
        self._running = True
        self._thread = threading.Thread(
            target=self._serve, daemon=True
        )
        self._thread.start()

    def _serve(self):
        while self._running:
            try:
                conn, addr = self._sock.accept()
                t = threading.Thread(
                    target=self._handle, args=(conn,), daemon=True
                )
                t.start()
            except socket.timeout:
                continue
            except Exception:
                break

    def _handle(self, conn):
        conn.settimeout(5.0)
        try:
            while self._running:
                data = conn.recv(65536)
                if not data: break
                try:
                    payload = json.loads(data.decode())
                except json.JSONDecodeError:
                    conn.sendall(json.dumps({'status': 'error', 'error': 'invalid_json'}).encode())
                    continue
                
                self.received_commands.append(payload)
                action = payload.get('action', '')
                if action == 'discover':
                    response = {
                        'status': 'ok',
                        'token': self.token,
                        'version': '2.0.0',
                        'protocol': '2',
                        'port': self.port,
                        'dsp_port': 9002
                    }
                elif payload.get('token') != self.token:
                    response = {'status': 'error', 'error': 'invalid_token'}
                elif action == 'ping':
                    response = {'id': payload.get('id'), 'status': 'ok',
                               'result': {'pong': True}}
                elif action == 'get_bpm':
                    response = {'id': payload.get('id'), 'status': 'ok',
                               'result': {'bpm': 124.0}}
                elif action == 'transport_play':
                    response = {'id': payload.get('id'), 'status': 'ok',
                               'result': {'playing': True}}
                else:
                    response = {'id': payload.get('id'), 'status': 'ok',
                               'result': {}}
                conn.sendall(json.dumps(response).encode())
        except Exception:
            pass
        finally:
            conn.close()

    def stop(self):
        self._running = False
        if self._sock:
            try:
                self._sock.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
            self._sock.close()
        if self._thread:
            self._thread.join(timeout=1)

@pytest.fixture
def server():
    s = MockAntigravityServer(port=0)
    s.start()
    time.sleep(0.05)
    yield s
    s.stop()
    time.sleep(0.05)

def test_handshake_discover(server):
    sock = socket.socket()
    sock.connect(('127.0.0.1', server.port))
    payload = {'action': 'discover', 'protocol': '2'}
    sock.sendall(json.dumps(payload).encode())
    response = json.loads(sock.recv(65536).decode())
    assert response['status'] == 'ok'
    assert 'token' in response
    assert response['token'] == MOCK_TOKEN
    sock.close()

def test_token_invalido_rechazado(server):
    sock = socket.socket()
    sock.connect(('127.0.0.1', server.port))
    payload = {'action': 'discover', 'protocol': '2'}
    sock.sendall(json.dumps(payload).encode())
    response = json.loads(sock.recv(65536).decode())
    token = response['token']
    
    payload2 = {'action': 'ping', 'token': 'bad_token'}
    sock.sendall(json.dumps(payload2).encode())
    resp2 = json.loads(sock.recv(65536).decode())
    
    assert resp2['status'] == 'error'
    assert 'token' in resp2.get('error', '').lower() or 'invalid' in resp2.get('error', '').lower()
    sock.close()

def test_ping_con_token_valido(server):
    sock = socket.socket()
    sock.connect(('127.0.0.1', server.port))
    sock.sendall(json.dumps({'action': 'discover', 'protocol': '2'}).encode())
    response = json.loads(sock.recv(65536).decode())
    token = response['token']
    
    sock.sendall(json.dumps({'action': 'ping', 'token': token}).encode())
    resp2 = json.loads(sock.recv(65536).decode())
    assert resp2['status'] == 'ok'
    assert resp2['result']['pong'] is True
    sock.close()

def test_get_bpm_retorna_numero(server):
    sock = socket.socket()
    sock.connect(('127.0.0.1', server.port))
    sock.sendall(json.dumps({'action': 'discover', 'protocol': '2'}).encode())
    response = json.loads(sock.recv(65536).decode())
    token = response['token']
    
    sock.sendall(json.dumps({'action': 'get_bpm', 'token': token}).encode())
    resp2 = json.loads(sock.recv(65536).decode())
    assert resp2['result']['bpm'] == 124.0
    sock.close()

def test_transport_play_retorna_playing(server):
    sock = socket.socket()
    sock.connect(('127.0.0.1', server.port))
    sock.sendall(json.dumps({'action': 'discover', 'protocol': '2'}).encode())
    response = json.loads(sock.recv(65536).decode())
    token = response['token']
    
    sock.sendall(json.dumps({'action': 'transport_play', 'token': token}).encode())
    resp2 = json.loads(sock.recv(65536).decode())
    assert resp2['result']['playing'] is True
    sock.close()

def test_json_invalido_manejado(server):
    sock = socket.socket()
    sock.connect(('127.0.0.1', server.port))
    sock.sendall(b'invalid_json')
    resp = json.loads(sock.recv(65536).decode())
    assert resp['status'] == 'error'
    assert 'json' in resp['error'].lower()
    sock.close()

def test_reconexion_tras_desconexion(server):
    sock = socket.socket()
    sock.connect(('127.0.0.1', server.port))
    sock.sendall(json.dumps({'action': 'discover', 'protocol': '2'}).encode())
    sock.recv(65536)
    sock.close()
    
    sock2 = socket.socket()
    sock2.connect(('127.0.0.1', server.port))
    sock2.sendall(json.dumps({'action': 'discover', 'protocol': '2'}).encode())
    resp = json.loads(sock2.recv(65536).decode())
    assert resp['status'] == 'ok'
    sock2.close()

def test_multiples_clientes_simultaneos(server):
    def worker():
        s = socket.socket()
        s.connect(('127.0.0.1', server.port))
        s.sendall(json.dumps({'action': 'discover', 'protocol': '2'}).encode())
        resp = json.loads(s.recv(65536).decode())
        tok = resp['token']
        s.sendall(json.dumps({'action': 'ping', 'token': tok}).encode())
        resp2 = json.loads(s.recv(65536).decode())
        s.close()
        return resp2['status'] == 'ok'
        
    with ThreadPoolExecutor(max_workers=3) as ex:
        futures = [ex.submit(worker) for _ in range(3)]
        for f in futures:
            assert f.result() is True
