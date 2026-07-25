import pytest
import socket
import threading
import json
import time
import statistics
from concurrent.futures import ThreadPoolExecutor
from tests.integration.test_tcp_integration import MockAntigravityServer

STRESS_PORT = 19002

class TestLatencia:
    def setup_method(self):
        self.server = MockAntigravityServer(STRESS_PORT)
        self.server.start()
        time.sleep(0.1)

    def teardown_method(self):
        self.server.stop()

    def _make_client(self):
        sock = socket.socket()
        sock.settimeout(5.0)
        sock.connect(('127.0.0.1', STRESS_PORT))
        payload = json.dumps({'action':'discover','protocol':'2'})
        sock.sendall(payload.encode())
        resp = json.loads(sock.recv(65536).decode())
        token = resp['token']
        return sock, token

    def test_latencia_50_pings_bajo_50ms_promedio(self):
        sock, token = self._make_client()
        latencias = []
        for i in range(50):
            payload = json.dumps({
                'action': 'ping',
                'token': token,
                'protocol': '2',
                'id': f'ping_{i}'
            })
            start = time.monotonic()
            sock.sendall(payload.encode())
            sock.recv(65536)
            latencias.append((time.monotonic() - start) * 1000)
        sock.close()
        avg = statistics.mean(latencias)
        p95 = sorted(latencias)[int(len(latencias)*0.95)]
        assert avg < 50, f"Latencia promedio {avg:.1f}ms > 50ms"
        assert p95 < 100, f"P95 {p95:.1f}ms > 100ms"

    def test_5_clientes_concurrentes_sin_error(self):
        errores = []
        lock = threading.Lock()

        def cliente_worker(worker_id):
            try:
                sock, token = self._make_client()
                for i in range(10):
                    payload = json.dumps({
                        'action': 'get_bpm',
                        'token': token,
                        'protocol': '2',
                        'id': f'w{worker_id}_r{i}'
                    })
                    sock.sendall(payload.encode())
                    resp = json.loads(sock.recv(65536).decode())
                    if resp.get('status') != 'ok':
                        with lock:
                            errores.append(f"Worker {worker_id}: {resp}")
                sock.close()
            except Exception as e:
                with lock:
                    errores.append(str(e))

        with ThreadPoolExecutor(max_workers=5) as ex:
            futures = [ex.submit(cliente_worker, i) for i in range(5)]
            for f in futures:
                f.result(timeout=30)

        assert len(errores) == 0, f"Errores: {errores}"

    def test_servidor_vivo_despues_de_100_requests(self):
        sock, token = self._make_client()
        for i in range(100):
            payload = json.dumps({
                'action': 'ping',
                'token': token,
                'protocol': '2',
                'id': f'r{i}'
            })
            sock.sendall(payload.encode())
            sock.recv(65536)
            
        final = json.dumps({
            'action': 'ping', 'token': token,
            'protocol': '2', 'id': 'final'
        })
        sock.sendall(final.encode())
        resp = json.loads(sock.recv(65536).decode())
        assert resp['status'] == 'ok'
        sock.close()
