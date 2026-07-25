import json
import os

log_path = "/Users/jesusferrer/.gemini/antigravity-ide/brain/61347475-da54-4ab9-833a-0eed0af52285/.system_generated/logs/transcript.jsonl"
out_path = "/Users/jesusferrer/.gemini/antigravity-ide/scratch/ableton-ai-assistant/full_prompt.txt"

largest_content = ""
with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        step = json.loads(line)
        if step.get("type") == "USER_INPUT":
            content = step.get("content", "")
            if len(content) > len(largest_content):
                largest_content = content

with open(out_path, "w", encoding="utf-8") as out:
    out.write(largest_content)
print(f"Extracted largest prompt to {out_path} ({len(largest_content)} bytes)")
