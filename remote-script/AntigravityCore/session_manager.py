# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import logging

logger = logging.getLogger(__name__)

class SessionManager(object):
    """
    Maneja la inyección de plugins nativos y el control de parámetros
    microscópicos para tareas de mezcla avanzadas.
    """
    
    def __init__(self, song, application):
        self.song = song
        self.application = application # Necesario para acceder al Browser

    def add_native_device(self, track_index, device_path_name):
        """
        Inserta un dispositivo nativo en la pista especificada.
        Utiliza el browser para garantizar compatibilidad multiplataforma.
        Ej: device_path_name = "Audio Effects/EQ Eight"
        """
        try:
            track = self.song.tracks[track_index]
            browser = self.application.browser
            
            # Buscar el item en la librería nativa de Ableton
            # Esta es una aproximación genérica. La ruta exacta depende de la estructura interna del LOM
            # En Live 11/12, iterar por browser.audio_effects
            target_item = None
            for item in browser.audio_effects.iter_children:
                if device_path_name.lower() in item.name.lower():
                    target_item = item
                    break
                    
            if not target_item:
                return {"status": "error", "message": f"Device {device_path_name} not found in browser."}

            self.song.begin_undo_step()
            self.song.view.selected_track = track
            browser.load_item(target_item)
            self.song.end_undo_step()
            
            return {"status": "success", "message": f"Device {target_item.name} loaded on track {track_index}."}
        except Exception as e:
            self.song.end_undo_step()
            logger.error("Error adding device: %s", str(e))
            return {"status": "error", "message": str(e)}

    def set_device_parameter(self, track_index, device_index, param_name, value):
        """
        Modifica un parámetro específico de un dispositivo.
        """
        try:
            track = self.song.tracks[track_index]
            if device_index >= len(track.devices):
                return {"status": "error", "message": "Device index out of range."}
                
            device = track.devices[device_index]
            target_param = None
            
            for param in device.parameters:
                if param.name.lower() == param_name.lower():
                    target_param = param
                    break
                    
            if not target_param:
                return {"status": "error", "message": f"Parameter {param_name} not found on device {device.name}."}

            # Asegurar que el valor esté dentro de los límites del parámetro
            safe_value = max(target_param.min, min(target_param.max, float(value)))
            
            self.song.begin_undo_step()
            target_param.value = safe_value
            self.song.end_undo_step()
            
            return {"status": "success", "message": f"Parameter {param_name} set to {safe_value}."}
        except Exception as e:
            self.song.end_undo_step()
            logger.error("Error setting parameter: %s", str(e))
            return {"status": "error", "message": str(e)}
