import math
import random
import randomint
import transforms



num = 4
poslist = []
# 12/3 = 4 <- 4-deep tree
for i in range(2**num):
    emptyrow = []
    for j in range(num*3):
        emptyrow.append(0)
    poslist.append(list(emptyrow))


momentalist = []
# 12/3 = 4 <- 4-deep tree
for i in range(2**(num-1)):
    emptyrow = []
    for j in range(num*3):
        emptyrow.append(0)
    momentalist.append(list(emptyrow))

#momenta creation


for i in range(num-1): #iterate through columns (in sets of three)
    for j in range(2**(num-1)): #iterate through rows and set initial momenta to 1,0,0
        momentalist[j][0] = 1
    if i >= 1: #for all except initial momenta, do the splitting
        subdivdone = 0 #need to reset
        subdivs = (2**i)
        subdivsize = int(2**num/subdivs)
        for j in range(int(subdivs/2)):#iterate through subdivisions/2 (as pairs of subdivisions share momentum)
            subdivdone = subdivdone + 1
            xprev = momentalist[3*j][i*3-3] 
            yprev = momentalist[3*j][i*3-2]
            zprev = momentalist[3*j][i*3-1]
            momentax = transforms.momentasplit(xprev,yprev,zprev)[0]
            momentay = transforms.momentasplit(xprev,yprev,zprev)[1]
            momentaz = transforms.momentasplit(xprev,yprev,zprev)[2]
            print(j)
            print(i)
            for k in range(subdivsize):#identical outputs for everything here
                momentalist[(3*j)+k][i*3+2] = momentax
                momentalist[(3*j)+k][i*3+1] = momentay
                momentalist[(3*j)+k][i*3] = momentaz

print(momentalist)
