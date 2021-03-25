import os
ls = [i for i in os.listdir() if i.endswith('.txt')]

ls.sort()


with open('all_data.txt','w') as f:
    for j in ls:
        data = open(j).read()
        f.write(data)
        f.write('\n')