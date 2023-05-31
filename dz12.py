def check(value):
    # value.replace(' ')
    if '/0' in value:
        return True
    else:
        return False
    
path = r'lesson13_dz_file.txt'

with open(path, 'r') as fl:
    problem = fl.readlines()
    
with open(path, 'w') as fl:
    for i in problem:
        line = i.strip().replace(' ', '').replace('\n', '')
        if check(line) == True:
            solution = 'error'
        else:
            solution = eval(line)
        fl.write(f'{line} = {solution} \n')
        
