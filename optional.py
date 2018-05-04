
sorting_bin = [1,4,5,346,63,2,1,6657,34,6,7,2346,67,7,3,23,46,8,564]

print(sorting_bin)
check = 0
sort = input("Do you want to sort ascending or decending? (a or d) ")

if sort.casefold() == 'a' :
    while check+1 < len(sorting_bin):
        if sorting_bin[check] <= sorting_bin[check+1]:
            check += 1
        else:
            sorting_bin.append(sorting_bin[check])
            sorting_bin.pop(check)
            check=0
elif sort.casefold() == 'd' :
    while check+1 < len(sorting_bin):
        if sorting_bin[check] >= sorting_bin[check+1]:
            check += 1
        else:
            sorting_bin.append(sorting_bin[check])
            sorting_bin.pop(check)
            check=0
print(sorting_bin)



