vcounter = 0
counter = 0
sp_chars = "!@#$%^&*()-+?_=,<>/"
path = r'/Users/dzvinkahai-nyzhnyk/Documents/yasna/HILLEL/dz/HM_lesson12_text.txt'
vowels = ['а', 'е', 'i', 'о', 'и', 'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я', 'ë', 'э', 'ы']
with open(path, 'r', encoding = 'cp1251') as fl:
    line = fl.read().split()
    longestword = max(line, key=len)
    for i in vowels:
        if i in longestword:
            vcounter += 1
    counter = len(longestword)-vcounter
    for i in longestword:
        if i in sp_chars:
            counter -= 1
with open(path, 'a', encoding = 'cp1251') as fl:
    fl.write(longestword.upper())
    
print(longestword)
print(vcounter, counter)
