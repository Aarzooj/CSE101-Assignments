allowance=20000
sf=0.001 #saving fraction
r=0.5   #rate
month=int(input("Enter the months required"))    
cost=int(input("Enter the cost of laptop")) 
t=0
s=sf*allowance  #savings

def function(cost,month,r,sf):
    s=sf*allowance
    t=0
    p=s
    amount=0
    while t<month:
        amount=p*((1+r/100)**1)
        interest=amount-p
        p=p+interest+s
        t+=1
    return amount   
          
while function(cost,month,r,sf)<cost:
    sf+=0.001
else:
    print("The required saving fraction is:",sf)
    print("The required saving rate is:",sf*100,"%")      


   
            
        





