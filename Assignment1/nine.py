import math

a=10
b=1.05
c=1
d=1.06

def de(p):
    x=a-b*p
    demand=math.exp(x)
    
    return demand
def s(p):
    y=c+d*p
    supply=math.exp(y)
    
    return supply
p=1
while p>0:
    m=de(p)
    n=s(p)

    if m<=n:
        print("The price at which equilibrium is achieved",p)
        print("Demand",de(p))
        print("Supply",s(p))
        if m!=n:
           print(" No perfect equilibrium")
        break
    
    p=p+0.05*p


      
    
      