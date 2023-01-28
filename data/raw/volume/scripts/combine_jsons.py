import os
import json

# Get all the json files in the directory
json_files = [pos_json for pos_json in os.listdir(
    'data/volume_control') if pos_json.endswith('.json')]

print(json_files)

# Combine all files in the list
combined_json = {}
for file in json_files:
    with open(os.path.join('data/volume_control', file)) as f:
        combined_json.update(json.load(f))

# Save the combined json
with open('data/volume_control/combined_volume.json', 'w') as f:
    json.dump(combined_json, f)
