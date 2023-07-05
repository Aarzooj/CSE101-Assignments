wt=[(10,5),(20,5),(100,15),(40,10),(80,30),(50,20),(30,15)]
# A>80,A->=70,B>=60,B->=50,C>=40,C->=35,D>=30,F<30
f=open("IPmarks.txt","r")
final_marks=[]
roll_no=[]
grade=[]
for line in f:
    s=line.split(',')
    l=[]    
    for i in range(1,len(s)):
        l.append((int(s[i])/int(wt[i-1][0]))*int(wt[i-1][1]))
    for i in range(0,1):
        roll_no.append(s[i])           
    final_marks.append(sum(l))
def grades(n):
    if n>80:
        return 'A'
    elif n>=70 and n<=80:
        return 'A-'
    elif n>=60 and n<70:
        return 'B'
    elif n>=50 and n<60:
        return 'B-'
    elif n>=40 and n<50:
        return 'C'
    elif n>=30 and n<40:
        return 'C-'  
    elif n>=20 and n<30:
        return 'D'  
    else:
        return 'F'

for i in range(len(final_marks)):
    grade.append(grades(final_marks[i]))
f=open("IPgrades.txt","w")
for i in range(len(final_marks)):
    s1=str(roll_no[i])
    s2=','
    s3=str(final_marks[i])
    s4=','
    s5=str(grade[i])
    sf=s1+s2+s3+s4+s5
    f.write(sf)
    f.write('\n')
f.close()
   