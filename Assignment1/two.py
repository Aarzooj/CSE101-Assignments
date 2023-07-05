def equation1(x1,x2):
    a=8*x1+2*x2
    if a<=400:
        return x1,x2         
def equation2(x1,x2):
    b=2*x1+1*x2
    if b<=120:
        return x1,x2      
def profit(M,x1,x2):
    P=90*M+100*(x1-M)+25*M+30*(x2-M)
    return P

M=int(input("Enter the M:"))
f_profit=0
f_x1=0
f_x2=0
for x1 in range(0,51):
    
    for x2  in range(0,121):
        if equation1(x1,x2)and equation2(x1,x2):

        
           if profit(M,x1,x2)>f_profit:

            f_profit=profit(M,x1,x2)
            f_x1=x1
            f_x2=x2
                   
print("Maximum profit is:",f_profit)  
print("Number of tables:",f_x1)
print("Number of chairs:",f_x2)           


                 
            



