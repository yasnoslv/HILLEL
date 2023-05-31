# multiplication table
num = input("input number: ")
if not num.isdigit():
    print("invalid number")
else: 
    for i in range(1,10):
        product = int(num) * i
        print(f"{i}x{num}={product}")
        
# # exam marks summ
# sum = 0
# count = 0
# for grade in range(1,5):
#     grade = int(input("input grade: "))
#     if grade > 12 or grade < 0:
#         print("grade invalid")
#         break
#     else:
#         sum += grade
#         count += 1
# if count == 4:
#     print(sum)