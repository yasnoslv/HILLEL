from random import randint
import os

numlist = []
newfull = []
newnewfull = []
result = []

dirname = input('input folder name: ')
os.mkdir(dirname)

for i in range(randint(2,10)):
    list = []
    with open(f'{dirname}/file{i}.txt', 'w') as fl:
        for i in range(randint(1,10000)):
            num = randint(1, 1000)
            list.append(num)
            fl.write(f'{str(num)} ')
    numlist.append(list)

for lst in numlist:
    part = []
    [part.append(i) for i in lst if i not in part]
    newfull.append(part)

for i in newfull:
    for el in i:
        newnewfull.append(el)
        
for i in newnewfull:
    if newnewfull.count(i) == len(numlist):
        if i not in result:
            result.append(i)
with open(f'{dirname}/result.txt', 'w') as fl:
    fl.write(str(result))