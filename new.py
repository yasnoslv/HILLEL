from random import randint
import os

allnum = [i for i in range(1, 1000)]
dirname = input('input folder name: ')
os.mkdir(dirname)

for i in range(randint(2, 10)):
    with open(f'{dirname}/file{i}.txt', 'w') as fl:
        num = [randint(1,1000) for i in range(randint(1,10000))]
        fl.write(str(num))
        for el in allnum:
            if el not in num:
                allnum.remove(el)

with open(f'{dirname}/result.txt', 'w') as fl:
    fl.write(str(allnum))