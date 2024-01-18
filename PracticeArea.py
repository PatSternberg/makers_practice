def unique_elements(l):
    newList = []
    for i in l:
        if i not in newList:
            newList.append(i)
    print(newList)

unique_elements(['1', '1', '2', '3', '4', '3'])
