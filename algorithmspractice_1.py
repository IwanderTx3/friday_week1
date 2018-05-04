
names = ["Alex","John",'Mary','Steve','John','Steve']

def check_dups(names):
    uniques = []
    for check in names:
        if check not in uniques:
            uniques.append(check)            
    return uniques            


names = check_dups(names)
print(names)