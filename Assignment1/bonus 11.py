#construct a calculator of a whole number :
# computing the square,square root,cube,cuberoot,check for prime/composite,print its factorial,log,sin,cos,tan,exponential
import math
list=['square','sq_root','cube','cube_root','p_c','fact','logn','sinn','cosn']

n=int(input("Enter the number"))
x=input("Enter the operation from list")
def square(n):
    return n**2
def sq_root(n):
    return n**0.5
def cube(n):
    return n**3
def cube_root(n):
    return n**1/3
def p_c(n):
    if n==2:
        print("N is prime")
    elif n!=2:

        for i in range(2,n):
            if n%i==0:                
                print("N is composite")
                break
        else:
            print ("N is prime") 
            
                 
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def l(n):
    return math.log(n)
def sin(x):
    sum=0
    for i in range(1,100,4):
        sum+=(x**i)/fact(i)
    for i in range(3,100,4):
        sum=sum-((x**i)/fact(i))
    return sum
def cos(x):
    sum=1
    for i in range(2,100,4):
        sum=sum-((x**i)/fact(i))
    for i in range(4,100,4):
        sum=sum+((x**i)/fact(i))
    return sum 

if x=='square':
    print(square(n))
if x=='sq_root':
    print(sq_root(n))
if x=='cube':
    print(cube(n))
if x=='cube_root':
    print(cube_root(n))
if x=='p_c':
    p_c(n)
if x=='fact':
    print(fact(n))
if x=='logn':
    print(l(n))    
if x=='sinn':
    print(sin(n))
if x=='cosn':
    print(cos(n))


