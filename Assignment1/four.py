import math
def v(t):
    return (2000*((math.log(140000))-math.log(140000-2100*t)))-9.8*t

dt=0.25
distance=0
a=int(input("enter the initial time"))
b=int(input("enter the final time"))  
t=a
while t<=b:
    distance+=v(t)*dt
    t+=dt
print("distance",distance) 
     

     