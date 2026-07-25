class SessionManager:

    @staticmethod
    def get_device_params(track_idx, device_idx, ctx):
        if not ctx.get("song"): return []
        tracks = list(ctx["song"].tracks)
        if not (0 <= track_idx < len(tracks)): return []
        devices = list(tracks[track_idx].devices)
        if not (0 <= device_idx < len(devices)): return []
        
        dev = devices[device_idx]
        params = []
        for p in getattr(dev, "parameters", []):
            params.append({
                "name": getattr(p, "name", ""),
                "value": getattr(p, "value", 0.0),
                "min": getattr(p, "min", 0.0),
                "max": getattr(p, "max", 1.0)
            })
        return params

    @staticmethod
    def set_device_param(track_idx, device_idx, param_idx, value, ctx):
        if not ctx.get("song"): return False
        tracks = list(ctx["song"].tracks)
        if not (0 <= track_idx < len(tracks)): return False
        devices = list(tracks[track_idx].devices)
        if not (0 <= device_idx < len(devices)): return False
        
        dev = devices[device_idx]
        params = list(getattr(dev, "parameters", []))
        if not (0 <= param_idx < len(params)): return False
        
        p = params[param_idx]
        p_min = getattr(p, "min", 0.0)
        p_max = getattr(p, "max", 1.0)
        clamped = max(p_min, min(p_max, value))
        p.value = clamped
        return True

    @staticmethod
    def load_device(track_idx, device_name, ctx):
        if not ctx.get("application"): return False
        browser = getattr(ctx["application"], "browser", None)
        if not browser: return False
        
        found = False
        for efx in getattr(browser, "audio_effects", []):
            if getattr(efx, "name", "") == device_name: found = True
        for inst in getattr(browser, "instruments", []):
            if getattr(inst, "name", "") == device_name: found = True
            
        return found

    @staticmethod
    def get_rack_chains(track_idx, device_idx, ctx):
        if not ctx.get("song"): return []
        tracks = list(ctx["song"].tracks)
        if not (0 <= track_idx < len(tracks)): return []
        devices = list(tracks[track_idx].devices)
        if not (0 <= device_idx < len(devices)): return []
        
        dev = devices[device_idx]
        return list(getattr(dev, "chains", []))

    @staticmethod
    def set_sidechain(track_idx, device_idx, source_track_idx, ctx):
        if not ctx.get("song"): return False
        tracks = list(ctx["song"].tracks)
        if not (0 <= track_idx < len(tracks)) or not (0 <= source_track_idx < len(tracks)): return False
        devices = list(tracks[track_idx].devices)
        if not (0 <= device_idx < len(devices)): return False
        
        dev = devices[device_idx]
        if hasattr(dev, "sidechain_routing"):
            dev.sidechain_routing = source_track_idx
            return True
        return False

    @staticmethod
    def set_automation(track_idx, param_name, values, times, ctx):
        return True
