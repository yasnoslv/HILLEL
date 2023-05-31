from random import randint

# TASK 1
# list compr 10 random els
rannum = [randint(1,10) for i in range(10)]
# starter list
print(rannum)
# set - no repeated els => len - how many non repeated els
print(len(set(rannum)))

# # TASK 2
# rannum1 = [randint(1,10) for i in range(10)]
# rannum2 = [randint(1,10) for i in range(10)]
# # starter lists
# print(rannum1, rannum2)
# # find len of set of diff els in rannum1
# print(len(set(rannum1).difference(set(rannum2))))

# # TASK 3
# rannum1 = [randint(1,10) for i in range(10)]
# rannum2 = [randint(1,10) for i in range(10)]
# # find same els in both lists (+ alternative way)
# result = set(rannum1).intersection(set(rannum2))
# # result = set(rannum1) & set(rannum2)
# # starter lists
# print(rannum1, rannum2)
# # sort lowest > highest
# print(sorted(result))

