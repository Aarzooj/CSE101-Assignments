def f(x):
    A=x**3-(10.5)*x**2+(34.5)*x-35
    return A
def d(x):
    B=3*x**2-21*x+34.5
    return B 

def root(x0):
    x1=x0-(f(x0)/d(x0))
    return x1
x0=float(input("Enter a number"))
while True:
    if f(x0)<=0.2 and f(x0)>=(-0.2):
        print("A root is:",x0)
        break
    if f(x0)>10**20:
        print("Too long to compute")
        break

    x0=root(x0)    
    
   
    

   




