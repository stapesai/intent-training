# Description: This script removes duplicate lines from the raw data files

inp_file = 'data/raw/volume/increase_mixed.txt'
out_file = 'data/raw/volume/increase_mixed.txt'

with open(inp_file, 'r') as f:
    text = f.readlines()

# print((text))
# print(str(text[0]))

print('len of original list: ', len(text))

lines = set()
for line in text:
    line = line.strip().lower()
    lines.add(line)

print('len of set: ', len(lines))

with open(out_file, 'w') as f:
    for line in lines:
        f.write(line + '\n')
