def powerUP(nump, p):
    PUPdone = list(map(lambda x: x ** p, nump))
    return PUPdone

nump = [2, 4, 7, 13, 25]
p = 2
PUPdone = powerUP(nump, p)
print(f'Nump to the p power in this case is:' , PUPdone)