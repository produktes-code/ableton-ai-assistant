import random

class MidiGenerator:
    GROOVE_TEMPLATES = {
        "house": {
            "kick":    [(0.0,36,100),(1.0,36,95),(2.0,36,100),(3.0,36,95)],
            "snare":   [(1.0,38,90),(3.0,38,85)],
            "hihat":   [(i*0.5,42,70) for i in range(8)],
            "openhat": [(1.5,46,80),(3.5,46,75)]
        },
        "techno": {
            "kick":    [(0.0,36,110),(1.0,36,100),(2.0,36,110),(3.0,36,100)],
            "snare":   [(1.0,38,95),(3.0,38,90)],
            "hihat":   [(i*0.25,42,65) for i in range(16)],
            "perc":    [(0.5,39,80),(2.5,39,75)]
        },
        "trap": {
            "kick":    [(0.0,36,110),(0.75,36,80),(2.0,36,100),(2.5,36,75)],
            "snare":   [(1.0,38,100),(3.0,38,95)],
            "hihat":   [(i*0.25,42,55+(i%3)*10) for i in range(16)],
            "openhat": [(0.5,46,85),(1.5,46,70),(2.5,46,80)]
        },
        "dnb": {
            "kick":    [(0.0,36,110),(1.5,36,90),(2.75,36,85)],
            "snare":   [(0.5,38,100),(1.0,38,80),(2.5,38,95)],
            "hihat":   [(i*0.25,42,60) for i in range(16)]
        }
    }

    SCALES = {
        "major":      [0,2,4,5,7,9,11],
        "minor":      [0,2,3,5,7,8,10],
        "dorian":     [0,2,3,5,7,9,10],
        "phrygian":   [0,1,3,5,7,8,10],
        "lydian":     [0,2,4,6,7,9,11],
        "mixolydian": [0,2,4,5,7,9,10],
        "pentatonic": [0,2,4,7,9],
        "blues":      [0,3,5,6,7,10]
    }

    @staticmethod
    def validate_note(pitch, velocity, start, duration):
        if not (0 <= pitch <= 127):
            raise ValueError("Pitch out of range")
        if not (1 <= velocity <= 127):
            raise ValueError("Velocity out of range")
        if duration < 0:
            raise ValueError("Duration cannot be negative")
        if start < 0:
            raise ValueError("Start cannot be negative")
        return True

    @staticmethod
    def inject_notes(clip, notes):
        if hasattr(clip, "canonical_parent") and hasattr(clip.canonical_parent, "begin_undo_step"):
            song = clip.canonical_parent
        else:
            song = getattr(clip, "song", None)
            
        if song and hasattr(song, "begin_undo_step"):
            song.begin_undo_step()
            
        injected = 0
        try:
            valid_notes = []
            for n in notes:
                try:
                    MidiGenerator.validate_note(n["pitch"], n["velocity"], n["start"], n["duration"])
                    valid_notes.append(n)
                    injected += 1
                except ValueError:
                    pass
            if hasattr(clip, "add_new_notes"):
                clip.add_new_notes(tuple(valid_notes))
        finally:
            if song and hasattr(song, "end_undo_step"):
                song.end_undo_step()
                
        return injected

    @staticmethod
    def generate_groove(style, bars, bpm, humanize=False):
        if style not in MidiGenerator.GROOVE_TEMPLATES:
            raise ValueError("Style not found in templates")
            
        template = MidiGenerator.GROOVE_TEMPLATES[style]
        notes = []
        
        for bar in range(bars):
            for inst, hits in template.items():
                for hit in hits:
                    start, pitch, vel = hit
                    start += bar * 4.0
                    
                    if humanize:
                        start += random.uniform(-0.02, 0.02)
                        start = max(0.0, start)
                        vel += random.randint(-8, 8)
                        vel = max(1, min(127, vel))
                        
                    notes.append({
                        "pitch": pitch,
                        "velocity": vel,
                        "start": start,
                        "duration": 0.25
                    })
        return notes

    @staticmethod
    def generate_melody(root_note, scale, bars, density):
        if scale not in MidiGenerator.SCALES:
            raise ValueError("Scale not found")
            
        intervals = MidiGenerator.SCALES[scale]
        notes = []
        
        for bar in range(bars):
            for beat in range(16):
                if random.random() < density:
                    octave_offset = random.choice([-12, 0, 12])
                    pitch = root_note + random.choice(intervals) + octave_offset
                    pitch = max(0, min(127, pitch))
                    
                    notes.append({
                        "pitch": pitch,
                        "velocity": random.randint(70, 110),
                        "start": (bar * 4.0) + (beat * 0.25),
                        "duration": 0.25
                    })
        return notes

    @staticmethod
    def quantize_notes(notes, grid):
        for n in notes:
            n["start"] = round(n["start"] / grid) * grid
        return notes

    @staticmethod
    def transpose_notes(notes, semitones):
        for n in notes:
            n["pitch"] = max(0, min(127, n["pitch"] + semitones))
        return notes
