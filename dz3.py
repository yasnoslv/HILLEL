#TASK1
str1 = input("input word: ")
if str1 == str1[::-1]:
	print("yes")
else:
	print("no")


# #TASK2
# num = input("input a 2-digit number: ")
# if num[0] > num[1]:
# 	print(num[0],">",num[1])
# elif num[0] < num[1]:
# 	print(num[0],"<",num[1])
# else:
# 	print(num[0],"=",num[1])


# #TASK3
# password = input("input password: ")
# # password needs to contain at least one upper letter, 
# # lower letter, one number, and be more than 6 symbols long
# if not password.islower():
#     if not password.isupper():
#         if not password.isdigit():
#             if not password.isalpha():
#                 if len(password) > 6:
#                     print("password is safe")
#                 else:
#                     print("(len)password too easy")
#             else:
#                 print("(alpha)password too easy")
#         else:
#             print("(digit)password too easy")
#     else:
#         print("(upper)password too easy")
# else:
#     print("(lower)password too easy")