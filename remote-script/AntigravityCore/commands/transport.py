def load(registry, ctx):
    registry.register("ping", ping, {"description": "Ping", "params": {}, "returns": "dict"})
    registry.register("transport_play", transport_play, {"description": "Play", "params": {}, "returns": "bool"})
    registry.register("transport_stop", transport_stop, {"description": "Stop", "params": {}, "returns": "bool"})
    registry.register("transport_record", transport_record, {"description": "Record", "params": {}, "returns": "bool"})
    registry.register("set_bpm", set_bpm, {"description": "Set BPM", "params": {"bpm": "float"}, "returns": "float"})
    registry.register("get_bpm", get_bpm, {"description": "Get BPM", "params": {}, "returns": "float"})
    registry.register("get_position", get_position, {"description": "Get pos", "params": {}, "returns": "float"})
    registry.register("set_position", set_position, {"description": "Set pos", "params": {"beats": "float"}, "returns": "float"})
    registry.register("set_loop", set_loop, {"description": "Loop", "params": {"start": "float", "length": "float", "enabled": "bool"}, "returns": "bool"})
    registry.register("get_key", get_key, {"description": "Get Key", "params": {}, "returns": "dict"})
    registry.register("set_key", set_key, {"description": "Set Key", "params": {"root_note": "int", "scale_name": "str"}, "returns": "dict"})
    registry.register("set_time_signature", set_time_signature, {"description": "Time Sig", "params": {"numerator": "int", "denominator": "int"}, "returns": "bool"})
    registry.register("jump_to_next_cue", jump_to_next_cue, {"description": "Next cue", "params": {}, "returns": "bool"})
    registry.register("jump_to_prev_cue", jump_to_prev_cue, {"description": "Prev cue", "params": {}, "returns": "bool"})
    registry.register("continue_playing", continue_playing, {"description": "Continue", "params": {}, "returns": "bool"})
    registry.register("stop_all_clips", stop_all_clips, {"description": "Stop all", "params": {"quantized": "bool"}, "returns": "bool"})

def ping(params, ctx): return {"status": "ok", "message": "pong"}
def transport_play(params, ctx):
    if ctx.get("song"): ctx["song"].is_playing = True
    return True
def transport_stop(params, ctx):
    if ctx.get("song"): ctx["song"].is_playing = False
    return True
def transport_record(params, ctx):
    if ctx.get("song"): ctx["song"].record_mode = True
    return True
def set_bpm(params, ctx):
    bpm = float(params.get("bpm", 120))
    if not (20 <= bpm <= 999): raise ValueError("BPM fuera de rango (20-999)")
    if ctx.get("song"): ctx["song"].tempo = bpm
    return bpm
def get_bpm(params, ctx): return ctx["song"].tempo if ctx.get("song") else 120.0
def get_position(params, ctx): return ctx["song"].current_song_time if ctx.get("song") else 0.0
def set_position(params, ctx):
    beats = float(params.get("beats", 0))
    if ctx.get("song"): ctx["song"].current_song_time = beats
    return beats
def set_loop(params, ctx):
    if ctx.get("song"):
        if "start" in params: ctx["song"].loop_start = params["start"]
        if "length" in params: ctx["song"].loop_length = params["length"]
        if "enabled" in params: ctx["song"].loop = params["enabled"]
    return True
def get_key(params, ctx):
    song = ctx.get("song")
    if song and hasattr(song, "root_note"): return {"root_note": song.root_note, "scale_name": getattr(song, "scale_name", "")}
    return {"root_note": 0, "scale_name": "Major"}
def set_key(params, ctx):
    root_note = int(params.get("root_note", 0))
    if not (0 <= root_note <= 11): raise ValueError("root_note fuera de rango (0-11)")
    song = ctx.get("song")
    if song and hasattr(song, "root_note"):
        song.root_note = root_note
        if "scale_name" in params: song.scale_name = params["scale_name"]
    return {"root_note": root_note, "scale_name": params.get("scale_name", "Major")}
def set_time_signature(params, ctx):
    if ctx.get("song"):
        ctx["song"].signature_numerator = params.get("numerator", 4)
        ctx["song"].signature_denominator = params.get("denominator", 4)
    return True
def jump_to_next_cue(params, ctx):
    if ctx.get("song"): ctx["song"].jump_to_next_cue()
    return True
def jump_to_prev_cue(params, ctx):
    if ctx.get("song"): ctx["song"].jump_to_prev_cue()
    return True
def continue_playing(params, ctx):
    if ctx.get("song"): ctx["song"].continue_playing()
    return True
def stop_all_clips(params, ctx):
    if ctx.get("song"): ctx["song"].stop_all_clips(params.get("quantized", True))
    return True
