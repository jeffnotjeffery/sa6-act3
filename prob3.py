def maxfinder(num, judge):
    if not num:
        return None
    maxnum = num[0]
    for um in num[1:]:
        maxnum = judge(maxnum, um)
    return maxnum


numnumnum = [23, 14, 15, 657, 89, 2]
bestoftwo = lambda x, y: x if x > y else y
maximum = maxfinder(numnumnum, bestoftwo)
print(f'MaXiMuM nUmBeR:' , maximum)