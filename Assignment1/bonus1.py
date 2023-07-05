list1=["one","two","three","four","five","six","seven","eight","nine"]
list2=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
list3=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
list4=["hundred","thousand","ten-thousand","lac","ten-lac","crore","ten-crore"]
x=int(input("Enter the number less than 100 crore:"))
ones=x%10
x=x//10
tens=x%10
x=x//10
hundreds=x%10
x=x//10
thousands=x%10
x=x//10
tenthousand=x%10
x=x//10
lacs=x%10
x=x//10
tenlac=x%10
x=x//10
crore=x%10
x=x//10
tencrore=x%10
for i in range(0,10):
    if tencrore==0:
        if crore==0:
            break
        else:
            if crore==i:
                print(list1[i-1],"crore",end=" ")
    elif tencrore==1:
        
        if crore==i:
            print(list3[i],"crore",end=" ")
    elif tencrore==i:
        if crore==0:
            print(list2[i-2],"crore",end=" ")
        else:
            for j in range(0,10):    
                if crore==j:
                   print(list2[i-2],list1[j-1],"crore",end=" ")
for i in range(0,10):
    if tenlac==0:
        if lacs==0:
            break
        else:
            if lacs==i:
                print(list1[i-1],"lac",end=" ")
    elif tenlac==1:
    
        if lacs==i:
            print(list3[i],"lac",end=" ")
    elif tenlac==i:
        if lacs==0:
            print(list2[i-2],"lac",end=" ")
        else:    
            for j in range(0,10):
                if lacs==j:

                    print(list2[i-2],list1[j-1],"lac",end=" ")      
for i in range(0,10):
    if tenthousand==0:
        
        if thousands==0:
            
            break
        else:
        
            if thousands==i:
                                                 
                print(list1[i-1],"thousand",end=" ")
        
    elif tenthousand==1:
        
        if thousands==i:
            print(list3[i],"thousand",end=" ")
    elif tenthousand==i:
        if thousands==0:
            print(list2[i-2],"thousand",end=" ")
        else:    
            for j in range(0,10):

                if thousands==j:

                  print(list2[i-2],list1[j-1],"thousand",end=" ")  
for i in range(0,10):
    if hundreds==0:
        pass
    elif hundreds==i:
        print(list1[i-1],"hundred",end=" ")
if ones==0:
    
    for i in range(1,10):
        if tens==i:
            print(list2[i-2])
elif ones!=0:
    if tens==0:
        for i in range(ones+1):
              if ones==i:
                print(list1[i-1])
    elif tens==1:
        for i in range(ones+1):
            if ones==i:
                print(list3[i])
    else:
        for i in range(tens+1):
            if tens==i:
                print(list2[i-2],end=" ")
        for i in range(ones+1):
            if ones==i:
                print(list1[i-1])
if tencrore==0 and crore==0 and tenlac==0 and lacs==0 and tenthousand==0 and thousands==0 and hundreds==0 and tens==0 and ones==0:
    

    print("zero")
                
                
print()                       



       





  