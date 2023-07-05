f=open('addrbook.txt','r')
import ast
x=f.readlines()
if x==[]:
    f_dict={}
else:
    f_dict=ast.literal_eval(x[0])    

def add():
    dict={}
    address=input('Enter the address')
    phone=input('Enter the phone no.')
    email=input('Enter the email id')
    dict['address']=address
    dict['phone_no']=phone
    dict['email_id']=email
    return dict
options={'1':'Insert new entry','2':'Delete an entry','3':'Find entry by partial name','4':'Find entry by phone/email','5':'Exit'}
for x,y in options.items():
    print(x,":",y)
#x=input('enter')
#f.truncate(0)
while True:
    print('Select an option')    
    select=input('Enter the option')
    if select=='5':
        f=open('addrbook.txt','w')
        print(f_dict)
        s=str(f_dict)
        f.write(s)
        break
    else:
        if select=='1':
            name=input('Enter the name')
            if len(f_dict)>=1:
                for x,y in f_dict.items():
                    l=[]
                    if name==x:
                        l.append(f_dict[x])
                        f_dict[name]=add()
                        l.append(f_dict[name])
                        f_dict[x]=l
                        break
                else:
                    f_dict[name]=add()  
            else:
                f_dict[name]=add()    
        elif select=='2':
            n=input('Enter the entry to be deleted')
            
            if type(f_dict[n])==list:
                w=input('Enter address/email/phone')
                y=f_dict[n]
                for i in y:
                    for f,g in i.items():
                        if w==g:
                            y.remove(i)
                            print('Deleted Successfully')
                            break
            else:                        
                del f_dict[n]
                print('Deleted Successfully')

        elif select=='3':
            n=input('Enter the partial name')
            for x in f_dict.keys():
                if n in x:
                    print(x,f_dict[x])
                # s=x.split(' ')
                # for i in s:
                #     if i==n:
        elif select=='4':
            n=input('Enter phone/email')
            for x,y in f_dict.items():
                if type(y)==list:
                    for d in y:
                        for b,z in d.items():
                            if n==z:               
                                print(x,d)
                else:                
                    for i,j in y.items():
                        if n==j:
                            print(x,y)
f.close()                