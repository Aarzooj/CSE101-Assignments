f=open("Yearbook.txt","r")
items=f.readlines()
l=[]
for i in items:
    i=i.strip("\n")
    l.append(i)
for i in l:
    if i=="":
        l.remove(i) 
l_key=[]
for i in range(0,len(l),5):
    l[i]=l[i][0:len(l[i])-1]
    l_key.append(l[i])
l_sign=[]  
for i in l:
    if ',' in i:
        l_sign.append(i)
yearbook={}
for i in range(len(l_key)):
    d={}
    l=l_sign[4*i:4*i+4]
    for j in l:
        j=j.split(',')
        d[j[0]]=j[1]
    yearbook[l_key[i]]=d
print(yearbook)    
final_yearbook={} 
for x,y in yearbook.items():
    count1=0
    count0=0
    for j in y.values():
        if int(j)==1:
            count1+=1
        final_yearbook[x]=count1     
print('Students with no. of signatures:\n',final_yearbook)
max=0
min=4
for x,y in final_yearbook.items():
    if y>max:
        max=y
    if y<min:
        min=y 
maxlist=[]
minlist=[]          
for x,y in final_yearbook.items():
    if final_yearbook[x]==max:
        maxlist.append(x)       
    elif final_yearbook[x]==min:
        minlist.append(x)
print('Students with max signatures',maxlist)            
print('Students with min signatures',minlist) 
f.close()

    
