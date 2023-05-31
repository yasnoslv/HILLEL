
# find middle
str1 = input("string no.1: ")
str2 = input("string no.2: ")
str3 = input("string no.3: ")

if len(str1)%2!=0:
    print("str1 middle: ", str1[len(str1)//2])
else:
    a1=(len(str1)//2)-1
    b1=(len(str1)//2)+1
    print("str1 middle: ", str1[a1:b1])
if len(str2)%2!=0:
    print("str2 middle: ", str2[len(str2)//2])
else:
    a2=(len(str2)//2)-1
    b2=(len(str2)//2)+1
    print("str2 middle: ", str2[a2:b2])
if len(str3)%2!=0:
    print("str3 middle: ", str3[len(str3)//2])
else:
    a3=(len(str3)//2)-1
    b3=(len(str3)//2)+1
    print("str3 middle: ", str3[a3:b3])


# longest str

str1 = len(str1)
str2 = len(str2)
str3 = len(str3)

if str1 != str2 and str1 != str3 and str2 != str3:
    print('HERE')
    if str1 > str2 and str1 > str3:
        print("str1 is the longest")
    elif str2 > str1 and str2 > str3:
        print("str2 is the longest")
    elif str3 > str1 and str3 > str2:
        print("str3 is the longest")

elif str1 == str2 == str3:
    print("all the same")

else:
    print("else")
    if str1 == str2 and str1 > str3:
        print("str1 and str2 are the longest")
    elif str1 == str2 and str1 < str3:
        print("str3 is the longest")
    
    elif str2 == str3 and str2 > str1:
        print("str2 and str3 are the longest")
    elif str2 == str3 and str2 < str1:
        print("str1 is the longest")
    
    elif str1 == str3 and str1 > str2:
        print("str1 and str3 are the longest")
    elif str1 == str3 and str1 < str2:
        print("str2 is the longest")
        

# find sum
print("all sum: ", str1 + str2 + str3)
