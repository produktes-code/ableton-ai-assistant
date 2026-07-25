import pkgutil
import importlib

class CommandRegistry:
    def __init__(self, ctx=None):
        self._commands = {}
        self._command_metadata = {}
        self.ctx = ctx or {}

    def auto_discover(self):
        from . import commands
        # Find all modules in the commands package
        for loader, module_name, is_pkg in pkgutil.iter_modules(commands.__path__):
            if module_name.startswith('_'):
                continue
            try:
                mod = importlib.import_module(f".commands.{module_name}", package="AntigravityCore")
                if hasattr(mod, "load"):
                    mod.load(self, self.ctx)
            except Exception as e:
                print(f"Error loading {module_name}: {e}")

    def register(self, action, func, metadata):
        required_keys = {"description", "params", "returns"}
        for k in required_keys:
            if k not in metadata:
                raise ValueError(f"Metadata para {action} debe incluir '{k}'")
                
        self._commands[action] = func
        self._command_metadata[action] = metadata

    def _validate_params(self, action, provided_params):
        expected_params = self._command_metadata[action].get("params", {})
        
        # Validar parámetros inesperados (strict mode)
        for p in provided_params:
            if p not in expected_params:
                raise ValueError(f"Parámetro inesperado '{p}' para la acción '{action}'")
                
        # Validar tipos (basic)
        for p_name, expected_type_str in expected_params.items():
            if p_name in provided_params:
                val = provided_params[p_name]
                if "int" in expected_type_str:
                    try:
                        int(val)
                    except ValueError:
                        raise ValueError(f"Parámetro '{p_name}' debe ser int")
                elif "float" in expected_type_str:
                    try:
                        float(val)
                    except ValueError:
                        raise ValueError(f"Parámetro '{p_name}' debe ser float")
                elif "bool" in expected_type_str:
                    if not isinstance(val, bool):
                        raise ValueError(f"Parámetro '{p_name}' debe ser bool")
                elif "str" in expected_type_str:
                    if not isinstance(val, str):
                        raise ValueError(f"Parámetro '{p_name}' debe ser str")

    def dispatch(self, payload):
        action = payload.get("action")
        if not action:
            raise ValueError("Falta 'action'")
            
        if action not in self._commands:
            first_10 = list(self._commands.keys())[:10]
            raise ValueError(f"Action '{action}' no existe. Comandos disponibles incluyen: {first_10}")
            
        params = payload.get("params", {})
        if not isinstance(params, dict):
            params = {}
            
        self._validate_params(action, params)
        
        func = self._commands[action]
        return func(params, self.ctx)

    def list_commands(self):
        return {
            action: self._command_metadata[action]
            for action in self._commands
        }

    def get_command_count(self):
        return len(self._commands)
