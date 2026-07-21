# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import logging

logger = logging.getLogger(__name__)


class MidiGenerator(object):
    """
    Maneja la generación consciente del contexto y la inyección
    no destructiva de MIDI a través del LOM (Live Object Model).
    """

    def __init__(self, song):
        self.song = song

    def read_midi_clip(self, track_index, clip_index):
        """
        Lee las notas de un clip existente para usarlas como contexto.
        Retorna una lista de diccionarios con la información de las notas.
        """
        try:
            track = self.song.tracks[track_index]
            clip_slot = track.clip_slots[clip_index]
            if clip_slot.has_clip:
                clip = clip_slot.clip
                if clip.is_midi_clip:
                    # En Live 11/12, get_notes_extended es el estándar
                    # Retorna una tupla de notas, donde cada nota tiene pitch, time, duration, velocity, mute
                    notes = clip.get_notes_extended(0, 127, 0.0, clip.length)
                    note_data = []
                    for note in notes:
                        note_data.append(
                            {
                                "pitch": note.pitch,
                                "time": note.start_time,
                                "duration": note.duration,
                                "velocity": note.velocity,
                                "probability": getattr(
                                    note, "probability", 1.0
                                ),  # Live 11+
                            }
                        )
                    return {"status": "success", "notes": note_data}
            return {
                "status": "error",
                "message": "No valid MIDI clip found at specified index.",
            }
        except Exception as e:
            logger.error("Error reading MIDI clip: %s", str(e))
            return {"status": "error", "message": str(e)}

    def inject_midi_notes(self, track_index, clip_index, notes_data):
        """
        Inyecta nuevas notas en un clip de forma no destructiva.
        notes_data: lista de diccionarios [{pitch, time, duration, velocity, probability}]
        """
        try:
            track = self.song.tracks[track_index]
            clip_slot = track.clip_slots[clip_index]

            # Crear clip si no existe
            if not clip_slot.has_clip:
                clip_slot.create_clip(4.0)  # Default 4 bars (16 beats)

            clip = clip_slot.clip
            if not clip.is_midi_clip:
                return {"status": "error", "message": "Target is not a MIDI clip."}

            # Envolver en Undo Step nativo
            self.song.begin_undo_step()

            # Preparar las notas para la API (Live 11/12 usa Live.Clip.MidiNoteSpecification)
            import Live

            new_notes = []
            for n in notes_data:
                # E19: Clamp pitch (and other values) to valid ranges
                raw_pitch = n.get("pitch", 60)
                clamped_pitch = max(0, min(127, int(raw_pitch)))

                clamped_velocity = max(1, min(127, int(n.get("velocity", 100))))
                clamped_probability = max(
                    0.0, min(1.0, float(n.get("probability", 1.0)))
                )

                # Live.Clip.MidiNoteSpecification(start_time, duration, pitch, velocity, mute, probability)
                note_spec = Live.Clip.MidiNoteSpecification(
                    start_time=float(n.get("time", 0.0)),
                    duration=float(n.get("duration", 1.0)),
                    pitch=clamped_pitch,
                    velocity=clamped_velocity,
                    mute=False,
                    probability=clamped_probability,
                )
                new_notes.append(note_spec)

            clip.add_new_notes(tuple(new_notes))

            self.song.end_undo_step()
            return {"status": "success", "message": "Notes injected successfully."}
        except Exception as e:
            self.song.end_undo_step()
            logger.error("Error injecting MIDI notes: %s", str(e))
            return {"status": "error", "message": str(e)}
