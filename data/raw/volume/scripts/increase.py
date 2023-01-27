# Description: This script converts the text file to json file

import json
inp_file = 'data/raw/volume/increase_mixed.txt'
out_file_1 = 'data/volume-control/increase_volume.json'
out_file_2 = 'data/volume-control/increase_volume_to_max.json'

with open(inp_file, 'r') as f:
    lines = f.readlines()


def change_intent(intent):
    var = ['as clear as', 'as loud as', 'maximum',
           'loudest', 'highest', 'as distinct as', 'as audible as','all the way up','100','full blast','full','all the way to the right']
    for i in var:
        if i in intent:
            return True
    return False


data_1 = {}
data_2 = {}
for line in lines:
    if line:
        key = line.strip().replace('\n', '')
        if change_intent(key):
            value = {
                "intent": "volume.value",
                "entities": {
                    "volume": "volume_max"}
            }
            value = dict(value)
            data_2[key] = value
        else:
            value = {
                "intent": "volume.increase",
                "entities": {
                    "volume": "current_volume + volume_increment"}
            }

            value = dict(value)
            data_1[key] = value

# print(data)

with open(out_file_1, 'w') as f:
    f.write(json.dumps(data_1, indent=4))
with open(out_file_2, 'w') as f:
    f.write(json.dumps(data_2, indent=4))
