sorting_bin = [1,4,5,346,63,2,1,6657,34,6,7,2346,67,7,3,23,46,8,564]
print(sorting_bin)
def bubbleSort(sorting_bin):
    sort = input("Do you want to sort ascending or decending? (a or d) ")
    if sort == 'a' :
        for check in range(len(sorting_bin)-1,0,-1):
            for i in range(check):
                if sorting_bin[i] > sorting_bin[i+1]:
                    temp = sorting_bin[i]
                    sorting_bin[i] = sorting_bin[i+1]
                    sorting_bin[i+1] = temp
    elif sort == 'd' :
        for check in range(len(sorting_bin)-1,0,-1):
            for i in range(check):
                if sorting_bin[i] < sorting_bin[i+1]:
                    temp = sorting_bin[i]
                    sorting_bin[i] = sorting_bin[i+1]
                    sorting_bin[i+1] = temp
    else:
        print("Please select either a or d")
bubbleSort(sorting_bin)
print(sorting_bin)



