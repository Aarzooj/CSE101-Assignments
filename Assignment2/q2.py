list=[]
f_list=[]
def credit(n):
    if n[1].isdigit():
        if int(n[1])==1 or int(n[1])==2 or int(n[1])==4:
            return True
        else:
            print("Incorrect Credit",n[1],"in",n[0])    
    else:
        print("Incorrect Credit",n[1])   
def grade(n):
    g=['A+','A','A-','B','B-','C','C-','D','F']
    for i in g:
        if n[2]==i:
            return True
    else:
        print("Incorrect grade",n[2],"in",n[0])        
def course(n):
    l=[]
    if n[0].isalnum():
        for i in range(len(n[0])):
            if ord(n[0][i])<65:            
                l.append(n[0][0:i])
                l.append(n[0][i:len(n[0])])
                break
        if len(l)==2:
            if l[0].isupper() and l[1].isdigit():
                return True
            else:
                print("Invalid course_no",n[0])  
        else:
            print("Invalid course_no",n[0])    
    else:   
        print("Invalid course_no",n[0])    
def sgpa(list):    
    value=[('A+',10),('A',10),('A-',9),('B',8),('B-',7),('C',6),('C-',5),('D',4),('F',2)]
    total_credits=0
    for i in list:
        total_credits+=int(i[1])
    result=0    
    for i in list:
        for j in value:
            grade=0            
            if i[2]==j[0]:
                grade=j[1]
                result+=int(int(i[1])*int(grade))

    final="%.2f" % (result/total_credits)
    return final            

while True:
    x=input('Enter the course details')
    if x=='':
        break
    else:        
        x=tuple(map(str,x.split()))        
        a=False
        b=False
        c=False
        if credit(x)==True:
            a=True
        if course(x)==True:
            b=True
        if grade(x)==True:
            c=True
        if a==True and b==True and c==True:                    
            f_list.append(x)
        
f_list.sort()
for i in f_list:
    print(str(i[0])+':',i[2])
print(sgpa(f_list)) 