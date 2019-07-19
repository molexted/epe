import random
def transform(partlist, momentum, angle, num):
    a = 1
    b = 2
    c = 2

def momentasplit(x, y, z):
    magnitude = ((x**2.0+y**2.0+z**2.0)**.5)
    split = random.random() #how much momentum the first one gets
    xshare = random.random() #how much of momentum goes to x-dir
    yshare = random.random() #how much of momentum goes to y-dir
    zshare = random.random() #how much of momentum goes to z-dir
    xyznormalization=(xshare+yshare+zshare)/3 
    xshare = xshare*xyznormalization
    yshare = yshare*xyznormalization
    zshare = zshare*xyznormalization
    x1 = magnitude*split*xshare
    y1 = magnitude*split*yshare
    z1 = magnitude*split*zshare
    x2 = magnitude*(1-split)*(1-xshare)
    y2 = magnitude*(1-split)*(1-yshare)
    z2 = magnitude*(1-split)*(1-zshare)
    return(x1,y1,z1,x2,y2,z2)

    
