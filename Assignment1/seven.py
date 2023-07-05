allowance=20000
sf=0.1
r=0.5
initial_p=2000
t=0
def function(cost,sf,r,p):
    t=0
    amount=p
    while amount<cost:
        amount=p*((1+r/100)**1)
        interest=amount-p
        p=p+interest+initial_p
        t=t+1
        
    saving_left=amount-cost
    return t,saving_left  
cost=int(input("enter the cost"))    
print("months taken and savings left are",function(cost,0.1,0.5,2000))      
  



        
    






