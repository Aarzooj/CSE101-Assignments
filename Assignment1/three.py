xo=5.0
yo=5.0
y=yo
x=xo
distance=0
while True:
    n=int(input("Enter"))
    if n<=0:
        break
    else:
        if n>0 and n<=25:
            y=y+n
            distance+=n
        if n>=26 and n<=50:
            y=y-n
            distance+=n   
        if n>=51 and n<=75:
            x=x+n
            distance+=n        
        if n>=76:
            x=x-n
            distance+=n   
displacement=((x-xo)**2+(y-yo)**2)**0.5
print("Final coordinates are:",x,y)   
print("Distance traveled is",distance) 
print("Displacement is ",displacement)        
