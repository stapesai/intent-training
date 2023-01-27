import json

input_file='data/raw/volume/unmute.txt'
output_file='data/volume-control/unmute.json'

with open (input_file,'r') as f:
    reader=f.readlines()

data_out={}

for lines in reader:
    lines=lines.strip().lower()
    key=lines.replace('\n','')
    value={
            "intent": "volume.value",
            "entities": {
                "volume": "last_volume"
            }
        }
    data_out[key] = value

with open(output_file,'w') as f:
    json.dump(data_out,f,indent=4)
print("DONE!!")
    