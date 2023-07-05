import time
class Course:
    def __init__(self,course,credits):
        self.course=course
        self.credits=credits
        self.assessment=[]
        self.grades=['A','B','C','D','F']
        self.grading=[]
    def create_assessment(self,assessments):
        self.assessment.append(assessments)  
    def grading_policy(self,policy):
        self.grading=policy    
class Student:
    def __init__(self):
        self.gd={}
        self.lgrading=[]
        self.gfd={} 
        self.finalgrade={} 
    def upload(self):
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
    def doscoring(self):
        f1=open('marks.txt','r')
        for line in f1:
            sum=0
            line=line.split(',')
            for j in range(len(line)):
                line[j]=line[j].strip('\n')
            for i in range(1,len(line)-1):
                sum+=float(line[i])
            self.gd[line[0]]=sum  
        f1.close()         
    def upgrade_grading(self):
        # start1=time.time()
        # for i in range(1000):            
        for y in self.gd.values():
            self.lgrading.append(y)
        self.lgrading.sort()
        for j in range(len(x1.grading)):
            l=[]
            for i in self.lgrading:        
                if i>=(float(x1.grading[j])-2) and i<=(float(x1.grading[j])+2):
                    l.append(i)
            if l==[] or len(l)==1:
                self.finalgrade[x1.grades[j]]=x1.grading[j]
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
                        self.finalgrade[x1.grades[j]]=(l[j]+l[j+1])/2 
        for x,y in self.gd.items():
            for c,z in self.finalgrade.items():
                if y>=z:
                    self.gfd[x]=c
                    break
                elif y<40:
                    self.gfd[x]='F' 
        # end1=time.time()
        # time_taken=end1-start1
        # return time_taken

course=input('Enter course name') 
credits=input('Enter the course credits')   
x1=Course(course,credits)
d=[]
sum=0
while True:
    if sum==100:
        break
    else:
        l2=list(map(str,input('Enter the assessment and % weightage').split()))
        assess=l2[0]
        weight=int(l2[1])
        t=(assess,weight)
        x1.create_assessment(t)
        sum+=weight 
print('Decide the grading policy')
policy=list(map(int,input('Enter the grading policy').split()))
x1.grading_policy(policy)
y1=Student()
y1.upload()
y1.doscoring()
print(y1.upgrade_grading())
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
            print('course name,credit','=',course,credits)
            print('assessmennts and their weight','=',x1.assessment)
            print('grading policy','=',y1.finalgrade,'\n')
            print('Grading summary:')
            countA,countB,countC,countD,countF=0,0,0,0,0
            print(y1.gfd)
            for y in y1.gfd.values():
                if y=='A':
                    countA+=1
                if y=='B':
                    countB+=1
                if y=='C':
                    countC+=1
                if y=='D':
                    countD+=1
                if y=='F':
                    countF+=1            
            print('countA','=',countA)
            print('countB','=',countB)
            print('countC','=',countC)
            print('countD','=',countD)
            print('countF','=',countF)
        elif int(n)==2:
            f2=open('grades.txt','w')
            for x,y in y1.gd.items():
                s=""
                for g,z in y1.gfd.items():
                    if x==g:
                        s+=str(y)+':'+str(g)+','+str(z)
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
            for line in f3:
                line=line.split(',')
                for j in range(len(line)):
                    line[j]=line[j].strip('\n')
                if line[0]==n:
                    print(line[0:len(line)-1])
            for x,y in y1.gd.items():
                if x==n:
                    print('Total marks:',y1.gd[x])
            for b,z in y1.gfd.items():
                if b==n:
                    print('Grade:',y1.gfd[b])                
            f3.close()
            # end2=time.time()
            # time_taken2=end2-start2
            # print(time_taken2)

