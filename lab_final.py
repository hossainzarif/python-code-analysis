import math
from loguru import logger
import snoop

@snoop
def ab(z, y):
    return math.log2(z)/math.log2(y)
def cd(y,a,c,n):
    return y*n/a*c
@logger.catch
def me(a,b,c,d):
    a=ab(a,b)
    b=ab(b,a)
    c=ab(c,d)
    d=ab(c,d)
    return cd(a,b,c,d)
p=10
q=5
r=3
s=1
me(p,q,r,s)

