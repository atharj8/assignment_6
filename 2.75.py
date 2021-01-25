from sympy import *
#Question1
#part A
#f(x)={3 0<=x<=1}
#f(x)={4 1<x<=3}
#f(x)={5 3<x<=10}
def f(a):
    if(0<=a<=1):
        return 3
    elif(1<a<=3):
        return 4
    elif(3<a<=10):
        return 5
#solution
#As f(x) is mixture of constant functions it will be continuous at every point except points at which constant functions are changing their behaviour that is 1,3
#for 1:
#here we will check left and right limit at 1 if they exists and are  equal then f(x) is continous at 1 otherwise discontionous
x=symbols('x')
init_printing(use_unicode=True)
delta=0.000001
LHL=limit(f(1-delta),x,1,'-')
RHL=limit(f(1+delta),x,1,'+')
t=0
if(LHL==RHL):
   t=t+1
#for 3
#similarly
h=0
LHL=limit(f(3-delta),x,3,'-')
RHL=limit(f(3+delta),x,3,'+')
print('question partA:')
if(LHL==RHL):
   h=h+1
if(h==1 and t==1):
    print("the function is contionus at every point")
elif(h==0 and t==1):
    print("the function is contionus at every point except at 3")
elif(t==0 and h==1):
    print("the function is continous at every point except at 1")
else:
    print("the function is contionous at every point except at 1,3")




#Question1
#part B
#f(x)={2*x ; x<0}
#f(x)={0 ; 0<=x<=1}
#f(x)={4*x ; x>1}
def F(a):
    if(a<0):
        return 2*x
    elif(0<=a<=1):
        return 0
    elif(a>1):
        return 4*x
#solution
#As F(x) is mixture of constant and linear polynomial functions it will be continuous at every point except points at which constant functions are changing their behaviour that is 0,1
#for 0:
#here we will check left and right limit at 0 if they exists and are  equal then f(x) is continous at 0 otherwise discontionous
x=symbols('x')
init_printing(use_unicode=True)
delta=0.1
LHL=limit(F(0-delta),x,0,'-')
RHL=limit(F(0+delta),x,0,'+')
t=0
if(LHL==RHL):
   t=t+1
#for 1
#similarly
h=0
LHL=limit(F(1-delta),x,1,'-')
RHL=limit(F(1+delta),x,1,'+')
print('question partB:')
if(LHL==RHL):
   h=h+1
if(h==1 and t==1):
    print("the function is contionus at every point")
elif(h==0 and t==1):
    print("the function is contionus at every point except at 1")
elif(t==0 and h==1):
    print("the function is continous at every point except at 0")
else:
    print("the function is contionous at every point except at 0,1")






#Question1
#part C
#f(x)={-2 : x<-1}
#f(x)={2*x : -1<=x<=1}
#f(x)={2 : x>1}
def f(a):
    if(a<-1):
        return -2
    elif(-1<=a<=1):
        return 2*x
    elif(a>1):
        return 2
#solution
#As f(x) is mixture of constant and linear polynomial functions it will be continuous at every point except points at which constant functions are changing their behaviour that is 1,-1
#for -1:
#here we will check left and right limit at -1 if they exists and are  equal then f(x) is continous at -1 otherwise discontionous
x=symbols('x')
init_printing(use_unicode=True)
delta=0.000001
LHL=limit(f(-1-delta),x,-1,'-')
RHL=limit(f(-1+delta),x,-1,'+')
t=0
print('question partC:')
if(LHL==RHL):
   t=t+1
#for 1
#similarly
h=0
LHL=limit(f(1-delta),x,1,'-')
RHL=limit(f(1+delta),x,1,'+')
if(LHL==RHL):
   h=h+1
if(h==1 and t==1):
    print("the function is contionus at every point")
elif(h==0 and t==1):
    print("the function is contionus at every point except at 1")
elif(t==0 and h==1):
    print("the function is continous at every point except at -1")
else:
    print("the function is contionous at every point except at -1,1")
















