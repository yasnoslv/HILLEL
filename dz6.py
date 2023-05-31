width = int(input("input width: "))
height = int(input("input height: "))

print("#"*width)
for i in range(height-2):
    print('#'+' '*(width-2)+'#')
print("#"*width)