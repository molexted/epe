import math
import random
import randomint
import transforms

def createmlist(num,v):
    mlist = []
    for i in range(2**(num-1)):
        emptyrow = []
        for j in range(num):
            emptyrow.append(0)
        mlist.append(list(emptyrow))
    #print(2**(num-1))
    #mlist creation

    for i in range(num): #iterate through columns
        for j in range(2**(num-1)): #iterate through rows and set initial momenta to 1,0,0
            mlist[j][0] = v
            if i >= 1:
                mlist[j][i] = 0
    #applying forces onto each outcome

    for j in range(num): #columns
        reset = int(2**(num-1)/2**j) #reset: number of entries before restarting
        groups = int(2**(num-2)/reset) #magic number 2 due to each reset covering two entries
        for k in range(groups):
            randup = round((mlist[k*reset*2][j-1])*random.random(),2)
            randdown = round((mlist[k*reset*2][j-1])*1-randup,2)
            for i in range(reset): #sets of complementary vectors
                mlist[i+(k*reset*2)][j] = randup
                mlist[i+reset+(k*reset*2)][j] = randdown
    return(mlist)

num = 15 #depth of tree
vx = 1 #initial momentum

poslist = []

mlisttot = createmlist(num, vx)
print(mlisttot)

