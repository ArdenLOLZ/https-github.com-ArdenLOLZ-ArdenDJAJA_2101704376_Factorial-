import math
def hypotenuse(a , b ):
    #c = (a**2 + b**2)**(1/2)
    try:
        return math.sqrt(a**2 + b**2)
    except TypeError:
        return None
d = hypotenuse
print(d(2,3)) #print 2 numbers
print(d("2","3"))
print(d(2,"3"))
