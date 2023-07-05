import time
print('Create a course')
print('Enter the following details')
l1=list(map(str,input('Enter the course name and credits').split()))
cname=l1[0]
credits=int(l1[1])
d=[]
sum=0
while True:
    if sum==100:
        break
    else:
        l2=list(map(str,input('Enter the assessment and % weigthage').split()))
        assess=l2[0]
        weight=int(l2[1])
        t=(assess,weight)
        d.append(t)
        sum+=weight
print('Decide the grading policy')
#(A,B,C,D,F)
l3=list(map(int,input('Enter the grading policy').split()))
def upload():
    print('Upload the marks')
    f=open("marks.txt","w")
    while True:
        s=list(map(str,input('Enter rollono and marks').split()))
        if s!=[]:
            for j in range(len(s)):
                f.write(s[j])
                f.write(',')
            f.write('\n')    
        else:
            break
    f.close() 
    print('Uploaded successfully!')  
gd={}         
def doscoring():
    f1=open('marks.txt','r')
    for line in f1:
        sum=0
        line=line.split(',')
        for j in range(len(line)):
            line[j]=line[j].strip('\n')
        for i in range(1,len(line)-1):
            sum+=float(line[i])
        gd[line[0]]=sum  
    f1.close() 
lgrading=[]
gfd={} 
grades=['A','B','C','D','F']   
finalgrade={}   
def dograding():
    # start1=time.time()
    # for i in range(1000):
    for y in gd.values():
        lgrading.append(y)
    lgrading.sort()
    for j in range(len(l3)):
        l=[]
        for i in lgrading:        
            if i>=(float(l3[j])-2) and i<=(float(l3[j])+2):
                l.append(i)
        if l==[] or len(l)==1:
            finalgrade[grades[j]]=l3[j]
        else:
            l.sort()
            d=0
            diff=[]
            for k in range(0,len(l)-1):
                diff.append(l[k+1]-l[k])
                if (l[k+1]-l[k])>d:
                    d=l[k+1]-l[k]
            for j in range(len(diff)):
                if diff[j]==d:
                    finalgrade[grades[j]]=(l[j]+l[j+1])/2        
    for x,y in gd.items():
        for c,z in finalgrade.items():
            if y>=z:
                gfd[x]=c
                break
            elif y<40:
                gfd[x]='F'  
    # end1=time.time()
    # time_taken1=end1-start1
    # return time_taken1                                  
upload()
doscoring()
print(dograding())
print(gfd)
options={1:'Generate the summary',2:'Print the grades',3:'Search for a student record'}
for x,y in options.items():
    print(x,':',y)
while True:
    n=input('Select an option')
    if n=="":
        break
    else:
        if int(n)==1:
            print('Summary\n')
            print('course name,credit','=',cname,credits)
            print('assessmennts and their weight','=',d)
            print('grading policy','=',finalgrade,'\n')
            print('Grading summary:')
            countA,countB,countC,countD,countF=0,0,0,0,0
            for y in gfd.values():
                if y=='A':
                    countA+=1
                if y=='B':
                    countB+=1
                if y=='C':
                    countC+=1
                if y=='D':
                    countD+=1
                elif y=='F':
                    countF+=1            
            print('countA','=',countA)
            print('countB','=',countB)
            print('countC','=',countC)
            print('countD','=',countD)
            print('countF','=',countF)
        elif int(n)==2:
            f2=open('grades.txt','w')
            for x,y in gd.items():
                s=""
                for g,z in gfd.items():
                    if x==g:
                        s+=str(g)+':'+str(y)+','+str(z)
                        f2.write(s)
                        f2.write('\n')
            print('Grades,marks uploaded')            
            f2.close()
        elif int(n)==3:
            # start2=time.time()
            # q6=['2022001','2022002','2022003','2022001','2022002','2022001']
            # for i in range(len(q6)):
            f3=open('marks.txt','r')
            # n=q6[i]
            # n=input('Enter the rollno.')
            for line in f3:
                line=line.split(',')
                for j in range(len(line)):
                    line[j]=line[j].strip('\n')
                if line[0]==n:
                    print(line[0:len(line)-1])
            for x,y in gd.items():
                if x==n:
                    print('Total marks:',gd[x])
            for b,z in gfd.items():
                if b==n:
                    print('Grade:',gfd[b])                
            f3.close()
            #     end2=time.time()
            #     time_taken2=end2-start2
            # print(time_taken2)    


            





