import secrets
import json
import time
import re
from . import config

class SecurityGuard:
    def __init__(self):
        self.session_token = secrets.token_hex(32)
        self.requests_log = {}  # ip -> list of timestamps
        self.blacklist = {}     # ip -> unban_time
        
        self.metrics = {
            "commands_processed": 0,
            "errors": 0,
            "blacklisted_ips": 0
        }
        
        self.action_regex = re.compile(r"^[a-z][a-z0-9_]{0,63}$")

    def validate_token(self, token):
        if not token:
            return False
        return secrets.compare_digest(self.session_token, str(token))

    def check_rate_limit(self, ip, current_time):
        if ip in self.blacklist:
            if current_time < self.blacklist[ip]:
                return False
            else:
                del self.blacklist[ip]

        window_start = current_time - 1.0
        if ip not in self.requests_log:
            self.requests_log[ip] = []
        
        self.requests_log[ip] = [t for t in self.requests_log[ip] if t > window_start]
        
        if len(self.requests_log[ip]) >= config.RATE_LIMIT_REQS_PER_SEC:
            self.blacklist[ip] = current_time + config.BLACKLIST_DURATION_SEC
            self.metrics["blacklisted_ips"] += 1
            return False
            
        self.requests_log[ip].append(current_time)
        return True

    def validate_payload(self, raw_data, ip):
        current_time = time.time()
        
        if not self.check_rate_limit(ip, current_time):
            self.metrics["errors"] += 1
            return {"error": "rate_limited_or_blacklisted"}
            
        if len(raw_data) > config.MAX_MESSAGE_SIZE:
            self.metrics["errors"] += 1
            return {"error": "payload_too_large"}
            
        try:
            text_data = raw_data.decode('utf-8')
        except UnicodeDecodeError:
            self.metrics["errors"] += 1
            return {"error": "invalid_utf8"}
            
        try:
            payload = json.loads(text_data)
        except json.JSONDecodeError:
            self.metrics["errors"] += 1
            return {"error": "invalid_json"}
            
        if not isinstance(payload, dict):
            self.metrics["errors"] += 1
            return {"error": "payload_must_be_dict"}
            
        action = payload.get("action")
        if not action:
            self.metrics["errors"] += 1
            return {"error": "missing_action"}
            
        if not self.action_regex.match(str(action)):
            self.metrics["errors"] += 1
            return {"error": "invalid_action_format"}
            
        protocol = payload.get("protocol")
        if protocol != config.PROTOCOL_VERSION:
            self.metrics["errors"] += 1
            return {"error": "unsupported_protocol_version"}
            
        if action not in ("ping", "discover"):
            token = payload.get("token")
            if not self.validate_token(token):
                self.metrics["errors"] += 1
                return {"error": "invalid_token"}
                
        self.metrics["commands_processed"] += 1
        return {"success": True, "payload": payload}

    def get_metrics(self):
        return self.metrics
