f=open("pages.txt","r")
d={}
f_imp=[]
f_url=[]
for line in f:  
    x=line.split(":")   
    y=x[1].split(",")
    l=[]
    f_list=[]
    for i in y:
        i=i.rstrip('\n')
        i=i.lstrip('URL')
        l.append(i)
    z=x[0].split(',') 
    z[0]=z[0].lstrip('URL')  
    for j in l:
        if j not in f_list:
            f_list.append(j)
    d[z[0]]=f_list
    f_imp.append(z[1])
    f_url.append(z[0])    
f_values=[]
for y in d.values():
    f_values.append(y)    
def over_imp():
    lf=[]
    for x in d.keys():
        sum=0
        for y in d.values():
            for i in range(len(y)):
                if int(x)==int(y[i]):
                    sum+=float(f_imp[int(f_values.index(y))])/int(len(y))
        lf.append(sum)
    return lf 
d_final={}
for m in range(len(f_url)):
    f_url[m]='URL'+f_url[m]     
for k in range(len(over_imp())):
    d_final[f_url[k]]=over_imp()[k]
print(d_final)    
s_d_final = sorted([(y,x)
 for (x, y) in d_final.items()])
s_d_final=s_d_final[::-1]
N=int(input("Enter"))
for i in range(N):
    print(s_d_final[i])
f.close()
        
            

            





























f.close()