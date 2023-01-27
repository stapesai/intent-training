import random
import json
inp_file = 'data/raw/volume/set_by_value.txt'
out_file = 'data/volume-control/set_by_volume.json'


# Read the input file
with open(inp_file, 'r') as f:
    lines = f.readlines()

data_out = {}

for line in lines:
    line = line.strip().lower()
    for num in range(0, 101):
        key = line.replace('__', str(num))
        value = {
            "intent": "volume.value",
            "entities": {
                "volume": "{}".format(num)
            }
        }
        data_out[key] = value

# Randomise data_out dict
print("Randomising data_out dict")
data_out = dict(random.sample(data_out.items(), len(data_out)))

with open(out_file, 'w') as f:
    json.dump(data_out, f, indent=4)
