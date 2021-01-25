#find relation between a and b so that the given function is continous at x=3
#f(x)={ax+1 : x<=3
#        bx+3 : x>3}

from sympy import *
a=symbols('a')
x=symbols('x')
b=symbols('b')
init_printing(use_unicode=True)
def f(d):
    if(d<=3):
        return a*x+1
    elif(d>3):
        return b*x+3
#for f(x) to be continous at x=3
#left hand limit and right hand limit at x=3 must be equal
delta=0.01
LHL=limit(f(3-delta),x,3,'-')
RHL=limit(f(3+delta),x,3,'+')
eq1=Eq(LHL,1)
eq2=Eq(RHL,1)
q=solve((eq1,eq2),(a,b))
w=list(q.keys())
print(f"the relationship between a and b is given as:\n {w[0]-w[1]}={q[a]-q[b]}")

