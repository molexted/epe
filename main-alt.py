import math
import random
import randomint
import transforms

num = 4
poslist = []

momentalist = []
# 12/3 = 4 <- 4-deep tree
for i in range(2**(num-1)):
    emptyrow = []
    for j in range(num):
        emptyrow.append(0)
    momentalist.append(list(emptyrow))

#momenta creation


for i in range(num): #iterate through columns (in sets of three)
    for j in range(2**(num-1)): #iterate through rows and set initial momenta to 1,0,0
        momentalist[j][0] = 1
        if i >= 1:
            momentalist[j][i] = 5
print(momentalist)
