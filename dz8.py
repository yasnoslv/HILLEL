from random import randint

list = [randint(1,10) for i in range(randint(5, 10))]
even = []
summ, oddsum, evensum, counter = 0, 0, 0, 0

for i in list:
    summ += i
    if i % 2 == 0:
        evensum += i
    else:
        oddsum += i

    if counter % 2 == 0:
        even.append(i)
    counter += 1

print(f'original list: {list}')
print(f'even indexes: {even}')
print(f'all sum: {summ}')
print(f'odd sum: {oddsum}\neven sum: {evensum}')
print(f'max num: {max(list)}')
print(f'max num index: {list.index(max(list))}')
