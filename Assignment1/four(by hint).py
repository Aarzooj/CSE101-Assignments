a=int(input("Enter initial time"))
b=int(input("Enter final time"))
dt=0.25
t=a
import math
def velocity(t):
    v=(2000*(math.log(140000/(140000-2100*t))))-9.8*t
    return v
distance=0    
while t<=b-dt:
    distance=distance+(((velocity(t)+velocity(t+dt))/2)*dt)
    t+=dt
print("Distance traveled is",distance)    


