# TASK1
colors = ["red","blue","green","yellow","purple","pink","orange","brown","black","white","gray","gold","silver","navy blue","sky blue","lime green","teal","indigo","magenta","violet","khaki","salmon","crimson","lavender","plum","blue violet","olive","cyan","maroon","beige"]
list = []
counter = 0

while counter < 4:
    color = input("input color: ")
    if color not in colors:
        print("no such color exists")
    else:
        list.append(color)
        print(list)
        counter += 1
       
# # TASK2
# list = []
# result = ''
# while True:
#     number = input('enter a number: ')
#     if number.isnumeric():
#         list.append(number)
#         if int(number) % 2 != 0:
#             result = result + number + '; '
#     elif number == 'end':
#         break
#     else:
#         print('number invalid')
# print(result)

