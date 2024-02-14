def intersect(list1, list2): 
    tcesretni = list(filter(lambda x: x in list2, list1))
    return tcesretni

list1 = [6, 7, 8, 9, 10]
list2 = [1, 10, 4, 6, 9]
tcesretni = intersect(list1, list2)
print(f'The intersection of the two lists is:' , tcesretni)
