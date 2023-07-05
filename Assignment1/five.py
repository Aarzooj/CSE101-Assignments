pi=3.14
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact    
def sin(x):
    sum=0
    for i in range(1,100,4):
        sum+=(x**i)/factorial(i)
    for i in range(3,100,4):
        sum=sum-((x**i)/factorial(i))
    return sum
def cos(x):
    sum=1
    for i in range(2,100,4):
        sum=sum-((x**i)/factorial(i))
    for i in range(4,100,4):
        sum=sum+((x**i)/factorial(i))
    return sum
angle=int(input("enter the angle in degrees:"))
x=int(input("enter the distance from pole:"))
h=sin(angle*pi/180)/cos(angle*pi/180)*x
y=h/sin(angle*pi/180)
print("Height of the pole is",h,"meters")
print("Distance from the tip is",y,"meters")                     