import math
import random
import randomint
import transforms

randomint.randomintrange(5, 0, 10)

num = 4
poslist = []
# 12/3 = 4 <- 4-deep tree
for i in range(2**num):
    emptyrow = []
    for j in range(num*3):
        emptyrow.append(0)
    poslist.append(list(emptyrow))

print(poslist)

momentalist = []
# 12/3 = 4 <- 4-deep tree
for i in range(2**num):
    emptyrow = []
    for j in range(num*3):
        emptyrow.append(0)
    momentalist.append(list(emptyrow))

print(poslist)

#momenta creation

print(transforms.momentasplit(1,0,0))

for i in range(num): #iterate through columns (in sets of three)
    for j in range(2**num): #iterate through rows
        momentalist[j][0] = 1
    if i >= 1:
        subdivdone = 0
        print(i)
        subdivs = (2**i)
        subdivsize = (2**num/subdivs)
        print(subdivs)
        for j in range subdivs:
            subdivdone++
            for k in range subdivsize:

print(momentalist)
