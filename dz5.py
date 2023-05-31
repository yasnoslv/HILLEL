# TASK1
rangeinp = int(input("input triangle height: "))
if rangeinp > 15:
    print("height unavailable")
elif rangeinp < 1:
    print("height unavailable")
else:
    for i in range(rangeinp):
        print(' '*i + '*'*(rangeinp-i)+'*'*(rangeinp-(i+1)))

# # TASK2
# for i in range(1,10):
#     print(f'\t{i}', end = '')
# print('')
# for i in range(1,10):
#     print(i, end = '')
#     for k in range(1,10):
#         print(f'\t{k*i}', end = '')
#     print('')
