list1=["one","two","three","four","five","six","seven","eight","nine"]
list2=["zero","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
list3=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
x=int(input("Enter the number between 0 and 99:"))
ones=x%10
tens=x//10
if ones==0:
    for i in range(tens+1):
        if tens==i:
            print(list2[i])
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
                print(list2[i-1],end=" ")
        for i in range(ones+1):
            if ones==i:
                print(list1[i-1])
print()    















