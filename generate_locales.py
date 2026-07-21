import json
import os

keys = [f"key_{i}" for i in range(1, 34)]
locales = ["es", "en", "de", "uk", "ru", "zh", "ja"]
locales_dir = "electron-app/locales"
for loc in locales:
    data = {k: f"Value {loc} {k}" for k in keys}
    with open(os.path.join(locales_dir, f"{loc}.json"), "w") as f:
        json.dump(data, f, indent=2)
print("Locales generated")
