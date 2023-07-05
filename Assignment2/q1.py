menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
for i in range(1,len(menu)+1):
    print(i,menu[i-1][0],"Rs",menu[i-1][1])
order=[]
while True:   
    x=input("The the item no. and quantity desired")    
    if x=='':
        break
    else:
        x=list(map(int,x.split()))
        order.append(x)
sum1=0
sum2=0        
for i in order:
    for j in range(1,len(menu)+1):        
        if i[0]==j:
            sum1+=int(i[1])
            sum2+=int(i[1]*menu[j-1][1])
            print(str(menu[j-1][0])+",",str(i[1])+",","Rs",i[1]*menu[j-1][1])  
print("TOTAL"+",",sum1,"items"+",","Rs",sum2)
