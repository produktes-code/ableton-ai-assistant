def load(registry, ctx):
    registry.register("create_midi_clip", create_midi_clip, {"description": "Create", "params": {"track_index": "int", "slot_index": "int", "length": "float"}, "returns": "bool"})
    registry.register("fire_clip", fire_clip, {"description": "Fire", "params": {"track_index": "int", "slot_index": "int"}, "returns": "bool"})
    registry.register("stop_clip", stop_clip, {"description": "Stop", "params": {"track_index": "int", "slot_index": "int"}, "returns": "bool"})
    registry.register("delete_clip", delete_clip, {"description": "Delete", "params": {"track_index": "int", "slot_index": "int"}, "returns": "bool"})
    registry.register("duplicate_clip", duplicate_clip, {"description": "Duplicate", "params": {"track_index": "int", "slot_index": "int"}, "returns": "bool"})
    registry.register("set_clip_name", set_clip_name, {"description": "Name", "params": {"track_index": "int", "slot_index": "int", "name": "str"}, "returns": "bool"})
    registry.register("set_clip_color", set_clip_color, {"description": "Color", "params": {"track_index": "int", "slot_index": "int", "color": "int"}, "returns": "bool"})
    registry.register("get_clip_info", get_clip_info, {"description": "Info", "params": {"track_index": "int", "slot_index": "int"}, "returns": "dict"})
    registry.register("get_session_state", get_session_state, {"description": "State", "params": {}, "returns": "dict"})
    registry.register("fire_scene", fire_scene, {"description": "Fire scene", "params": {"scene_index": "int"}, "returns": "bool"})
    registry.register("set_clip_loop", set_clip_loop, {"description": "Loop", "params": {"track_index": "int", "slot_index": "int", "loop": "bool"}, "returns": "bool"})

def _get_slot(ctx, t_idx, s_idx):
    if not ctx.get("song"): return None
    tracks = list(ctx["song"].tracks)
    if not (0 <= t_idx < len(tracks)): raise ValueError("Track index out of range")
    slots = list(tracks[t_idx].clip_slots)
    if not (0 <= s_idx < len(slots)): raise ValueError("Slot index out of range")
    return slots[s_idx]

def _get_clip(ctx, t_idx, s_idx):
    slot = _get_slot(ctx, t_idx, s_idx)
    if slot and getattr(slot, "has_clip", False): return slot.clip
    raise ValueError("No clip in slot")

def create_midi_clip(params, ctx):
    slot = _get_slot(ctx, params["track_index"], params["slot_index"])
    if slot and not getattr(slot, "has_clip", False): slot.create_clip(params.get("length", 4.0))
    return True
def fire_clip(params, ctx):
    slot = _get_slot(ctx, params["track_index"], params["slot_index"])
    if slot: slot.fire()
    return True
def stop_clip(params, ctx):
    slot = _get_slot(ctx, params["track_index"], params["slot_index"])
    if slot: slot.stop()
    return True
def delete_clip(params, ctx):
    slot = _get_slot(ctx, params["track_index"], params["slot_index"])
    if slot and getattr(slot, "has_clip", False): slot.delete_clip()
    return True
def duplicate_clip(params, ctx):
    slot = _get_slot(ctx, params["track_index"], params["slot_index"])
    if slot and getattr(slot, "has_clip", False): slot.duplicate_clip_to(slot)
    return True
def set_clip_name(params, ctx):
    clip = _get_clip(ctx, params["track_index"], params["slot_index"])
    if clip: clip.name = params["name"]
    return True
def set_clip_color(params, ctx):
    clip = _get_clip(ctx, params["track_index"], params["slot_index"])
    if clip: clip.color = params["color"]
    return True
def get_clip_info(params, ctx):
    clip = _get_clip(ctx, params["track_index"], params["slot_index"])
    return {"name": getattr(clip, "name", "mock")} if clip else {}
def get_session_state(params, ctx): return {}
def fire_scene(params, ctx):
    if ctx.get("song"):
        scenes = list(ctx["song"].scenes)
        idx = params["scene_index"]
        if 0 <= idx < len(scenes): scenes[idx].fire()
    return True
def set_clip_loop(params, ctx):
    clip = _get_clip(ctx, params["track_index"], params["slot_index"])
    if clip: clip.looping = params["loop"]
    return True
