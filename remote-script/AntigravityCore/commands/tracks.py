def load(registry, ctx):
    registry.register("get_track_info", get_track_info, {"description": "Info", "params": {"track_index": "int"}, "returns": "dict"})
    registry.register("get_all_tracks", get_all_tracks, {"description": "All tracks", "params": {}, "returns": "list"})
    registry.register("set_track_mute", set_track_mute, {"description": "Mute", "params": {"track_index": "int", "mute": "bool"}, "returns": "bool"})
    registry.register("set_track_solo", set_track_solo, {"description": "Solo", "params": {"track_index": "int", "solo": "bool"}, "returns": "bool"})
    registry.register("set_track_arm", set_track_arm, {"description": "Arm", "params": {"track_index": "int", "arm": "bool"}, "returns": "bool"})
    registry.register("set_track_volume", set_track_volume, {"description": "Volume", "params": {"track_index": "int", "volume": "float"}, "returns": "bool"})
    registry.register("set_track_pan", set_track_pan, {"description": "Pan", "params": {"track_index": "int", "pan": "float"}, "returns": "bool"})
    registry.register("set_track_name", set_track_name, {"description": "Name", "params": {"track_index": "int", "name": "str"}, "returns": "bool"})
    registry.register("set_track_color", set_track_color, {"description": "Color", "params": {"track_index": "int", "color": "int"}, "returns": "bool"})
    registry.register("duplicate_track", duplicate_track, {"description": "Duplicate", "params": {"track_index": "int"}, "returns": "bool"})
    registry.register("delete_track", delete_track, {"description": "Delete", "params": {"track_index": "int"}, "returns": "bool"})
    registry.register("set_send", set_send, {"description": "Send", "params": {"track_index": "int", "send_index": "int", "value": "float"}, "returns": "bool"})

def _get_track(ctx, idx):
    if not ctx.get("song"): return None
    tracks = list(ctx["song"].tracks)
    if not (0 <= idx < len(tracks)): raise ValueError("Track index out of range")
    return tracks[idx]

def get_track_info(params, ctx):
    t = _get_track(ctx, params["track_index"])
    return {"name": getattr(t, "name", "mock_track")} if t else {}
def get_all_tracks(params, ctx): return []
def set_track_mute(params, ctx):
    t = _get_track(ctx, params["track_index"])
    if t: t.mute = params["mute"]
    return True
def set_track_solo(params, ctx):
    t = _get_track(ctx, params["track_index"])
    if t: t.solo = params["solo"]
    return True
def set_track_arm(params, ctx):
    t = _get_track(ctx, params["track_index"])
    if t and getattr(t, "can_be_armed", True): t.arm = params["arm"]
    return True
def set_track_volume(params, ctx):
    vol = float(params["volume"])
    if not (0.0 <= vol <= 1.0): raise ValueError("Volume out of range (0-1)")
    t = _get_track(ctx, params["track_index"])
    if t and hasattr(t, "mixer_device"): t.mixer_device.volume.value = vol
    return True
def set_track_pan(params, ctx):
    pan = float(params["pan"])
    if not (-1.0 <= pan <= 1.0): raise ValueError("Pan out of range (-1 to 1)")
    t = _get_track(ctx, params["track_index"])
    if t and hasattr(t, "mixer_device"): t.mixer_device.panning.value = pan
    return True
def set_track_name(params, ctx):
    t = _get_track(ctx, params["track_index"])
    if t: t.name = params["name"]
    return True
def set_track_color(params, ctx):
    t = _get_track(ctx, params["track_index"])
    if t: t.color = params["color"]
    return True
def duplicate_track(params, ctx):
    if ctx.get("song"): ctx["song"].duplicate_track(params["track_index"])
    return True
def delete_track(params, ctx):
    if ctx.get("song"): ctx["song"].delete_track(params["track_index"])
    return True
def set_send(params, ctx):
    t = _get_track(ctx, params["track_index"])
    if t and hasattr(t, "mixer_device"):
        s_idx = params["send_index"]
        if 0 <= s_idx < len(t.mixer_device.sends):
            t.mixer_device.sends[s_idx].value = params["value"]
    return True
