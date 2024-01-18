def unique_elements(l):
    uniqueList = l
    uniqueList.sort()
    for i in uniqueList:
        compare_dex = uniqueList.index(i)
        if (compare_dex != -1) and (uniqueList[compare_dex] == uniqueList[compare_dex + 1]):
            del uniqueList[compare_dex]
    print(uniqueList)

unique_elements(['1', '2', '2', '3'])