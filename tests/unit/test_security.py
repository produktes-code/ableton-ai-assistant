import sys
import os
import json
import time
from unittest.mock import MagicMock

# Mockear el módulo ableton.v3
sys.modules['ableton'] = MagicMock()
sys.modules['ableton.v3'] = MagicMock()
sys.modules['ableton.v3.control_surface'] = MagicMock()

# Agregar el directorio actual al path para importar módulos locales
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "remote-script")))

from AntigravityCore import config
from AntigravityCore.security import SecurityGuard

def test_security_module():
    print("--- INICIANDO TESTS DE SEGURIDAD (FASE 1) ---")
    guard = SecurityGuard()
    
    # Test 1: Validate payload too large
    large_data = b"x" * (config.MAX_MESSAGE_SIZE + 1)
    res = guard.validate_payload(large_data, "127.0.0.1")
    assert res.get("error") == "payload_too_large", f"Falló test payload_too_large: {res}"
    print("✅ Test 1 pasado: payload_too_large")

    # Test 2: Invalid UTF-8
    res = guard.validate_payload(b"\xff\xfe", "127.0.0.1")
    assert res.get("error") == "invalid_utf8", f"Falló test invalid_utf8: {res}"
    print("✅ Test 2 pasado: invalid_utf8")

    # Test 3: Invalid JSON
    res = guard.validate_payload(b"{bad json}", "127.0.0.1")
    assert res.get("error") == "invalid_json", f"Falló test invalid_json: {res}"
    print("✅ Test 3 pasado: invalid_json")

    # Test 4: Payload is not dict
    res = guard.validate_payload(b"[]", "127.0.0.1")
    assert res.get("error") == "payload_must_be_dict", f"Falló test payload_must_be_dict: {res}"
    print("✅ Test 4 pasado: payload_must_be_dict")

    # Test 5: Missing action
    res = guard.validate_payload(b'{"protocol": 2}', "127.0.0.1")
    assert res.get("error") == "missing_action", f"Falló test missing_action: {res}"
    print("✅ Test 5 pasado: missing_action")

    # Test 6: Invalid action format
    res = guard.validate_payload(b'{"action": "Action!", "protocol": 2}', "127.0.0.1")
    assert res.get("error") == "invalid_action_format", f"Falló test invalid_action_format: {res}"
    print("✅ Test 6 pasado: invalid_action_format")

    # Test 7: Invalid protocol
    res = guard.validate_payload(b'{"action": "ping", "protocol": 1}', "127.0.0.1")
    assert res.get("error") == "unsupported_protocol_version", f"Falló test unsupported_protocol_version: {res}"
    print("✅ Test 7 pasado: unsupported_protocol_version")

    # Test 8: Valid discover without token
    res = guard.validate_payload(b'{"action": "discover", "protocol": 2}', "127.0.0.1")
    assert res.get("success") is True, f"Falló test valid discover: {res}"
    print("✅ Test 8 pasado: valid discover without token")

    # Test 9: Action requires token, but missing
    res = guard.validate_payload(b'{"action": "custom_action", "protocol": 2}', "127.0.0.1")
    assert res.get("error") == "invalid_token", f"Falló test missing_token: {res}"
    print("✅ Test 9 pasado: missing token on protected action")

    # Test 10: Valid action with correct token
    token = guard.session_token
    valid_payload = json.dumps({"action": "custom_action", "protocol": 2, "token": token}).encode('utf-8')
    res = guard.validate_payload(valid_payload, "127.0.0.1")
    assert res.get("success") is True, f"Falló test valid action: {res}"
    print("✅ Test 10 pasado: valid action with token")

    # Test 11: Rate limiting
    print("   Ejecutando test de rate limit, por favor espere...")
    success_count = 0
    fail_count = 0
    for _ in range(120):
        res = guard.validate_payload(b'{"action": "ping", "protocol": 2}', "192.168.1.100")
        if res.get("success"):
            success_count += 1
        elif res.get("error") == "rate_limited_or_blacklisted":
            fail_count += 1
    
    assert success_count <= config.RATE_LIMIT_REQS_PER_SEC, f"Rate limit excedido: {success_count} exitosos"
    assert fail_count > 0, "No hubo fallos por rate limit"
    print("✅ Test 11 pasado: rate limiting")
    
    metrics = guard.get_metrics()
    print(f"Métricas finales: {metrics}")
    
    print("--- TODOS LOS TESTS PASARON CORRECTAMENTE ---")

if __name__ == "__main__":
    test_security_module()
