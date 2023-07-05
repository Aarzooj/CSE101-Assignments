pop=[50,1450,1400,1700,1500,600,1200]

def p(x,z,n):
    global pn
    pn=x
    
    growth_rate=z-0.1*(n-1)
    pn=pn+pn*(growth_rate/100)

    return pn   

x1,x2,x3,x4,x5,x6,x7=50,1450,1400,1700,1500,600,1200 #populations
z1,z2,z3,z4,z5,z6,z7=2.5,2.1,1.7,1.3,0.9,0.5,0.1 #growth rates
f_population=0
n=1
while n>=1:
    a=p(x1,z1,n)
    b=p(x2,z2,n)
    c=p(x3,z3,n)
    d=p(x4,z4,n)
    e=p(x5,z5,n)
    f=p(x6,z6,n)
    g=p(x7,z7,n)
    sum=a+b+c+d+e+f+g
    if sum<f_population:
        break    
    elif sum>f_population:
        f_population=sum
        
        x1=a
        x2=b
        x3=c
        x4=d
        x5=e
        x6=f
        x7=g 
        n+=1 
print("The max popultion possible is",f_population,"million")   
print("The year after which it is possible is",n-1)     
sum=0
for i in pop:
    sum=sum+i
print("The current total population is",sum,"million")