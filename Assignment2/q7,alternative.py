book={}
f=open("addrbook.txt","a+")
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
        print(book)
        for x,y in book.items():
            if type(y)!=list:                
                f.writelines([x,',',y["address"],',',y["phone_no"],",",y["email_id"]])
                f.write('\n')
            elif type(y)==list:
                for i in y:
                    f.writelines([x,',',i["address"],',',i["phone_no"],",",i["email_id"]])
                    f.write('\n')
        break                
    else:
        if select=='1':
            name=input('Enter the name')
            if len(book)>=1:
                for x,y in book.items():
                    l=[]
                    if name==x:
                        l.append(book[x])
                        book[name]=add()
                        l.append(book[name])
                        book[x]=l
                        break
                else:
                    book[name]=add()  
            else:
                book[name]=add()                     
        elif select=='2':
            f.seek(0,0)
            n=input('Enter the entry to be deleted')
            items=f.readlines()
            count=0
            for j in items:
                s=j.split(',')
                if s[0]==n:
                    count+=1
            if count==1:        
                itemsc=items.copy()  
                for i in items:
                    s=i.split(',')
                    if s[0]==n:
                        itemsc.remove(i)
                print('Deleted Successfully')
                f=open("addrbook.txt","w")                 
                for i in itemsc:
                    f.write(i)
            else:
                ask=input('Enter address/email/phone') 
                itemsc=items.copy()  
                for i in items:
                    s=i.split(',')
                    if s[0]==n:
                        for j in range(len(s)):
                            if s[j].rstrip('\n')==ask:
                                itemsc.remove(i)
                print('Deleted Successfully')
                f=open("addrbook.txt","w")                 
                for i in itemsc:
                    f.write(i)
            #  f.write('\n')                
        elif select=='3':
            f.seek(0,0)            
            items=f.readlines()
            n=input('Enter the first/last name')
            for i in items:
                s=i.split(',')
                full_name=s[0].split(' ')
                for j in range(len(full_name)):
                    if full_name[j]==n:
                        print(i)            
        elif select=='4':
            f.seek(0,0)            
            items=f.readlines()
            n=input('Enter phone/email')
            for i in items:
                s=i.split(',')
                for j in range(len(s)):
                    if s[j].rstrip("\n")==n:                        
                        print(i)
f.close()        

                    
