# import os
# list_ = []
# list_name = os.listdir('sorted')

# for i in list_name:
#     with open(f'sorted/{i}', encoding='utf-8') as f:
#         lines = f.readlines()
#         line = [i + '\n'] + [str(len(lines)) + '\n'] + lines
#         list_.append(line)
#     text = ' '.join(sum((sorted(list_, key=len)), [])

# # with open('all.txt', 'w', encoding='utf-8') as m:
# #     m.write('text')  


import os
ls = [i for i in os.listdir() if i.endswith('.txt')]

ls.sort()


with open('all_data.txt','w') as f:
    for j in ls:
        data = open(j).read()
        f.write(data)
        f.write('\n')