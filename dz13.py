name = 'file.txt'
find = 'h'
def reverse_h(filename, char):
    with open(filename, 'r') as fl:
        read = fl.read()
        first = read.find(char)
        last = read.rfind(char)
        string = read[first+1:last]
        print(string[::-1])
        
reverse_h(name, find)
