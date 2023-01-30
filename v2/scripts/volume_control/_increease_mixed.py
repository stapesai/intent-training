input_file='./data/raw_data/volume_control/increase_mixed.txt'
increase_to_max='./data/raw_data/volume_control/increase_to_max.txt'
increase='./data/raw_data/volume_control/increase.txt'


with open(input_file,'r') as f:
    queries=f.readlines()

var = ['as clear as', 'as loud as', 'maximum',
           'loudest', 'highest', 'as distinct as', 'as audible as','all the way up','100','full blast','full','all the way to the right']

def categorise(intent):
    for i in var:
        if i in intent:
            return True
    return False

   
   
increase_to_max_list=[]
increase_list=[]

for query in queries:
    if categorise(query):
        increase_to_max_list.append(query)

    else:
        increase_list.append(query)

with open(increase_to_max,"w") as f:
    for j in increase_to_max_list:
        f.write(j)

with open(increase,"w") as f:
    for i in increase_list:
        f.write(i)

