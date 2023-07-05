f=open('sorted_data.txt')
f.readline()
l=[]   
for line in f:
    line=line.split(',')
    for i in range(len(line)):
        line[i]=line[i].lstrip(" ")
        line[i]=line[i].rstrip("\n")
    if line[0] not in l:
        l.append(line[0]) 
# print(l)                 
f.seek(0,0)
f.readline()
final={}
for line in f:
    line=line.split(',')
    for j in range(len(line)):
        line[j]=line[j].lstrip(" ")
        line[j]=line[j].rstrip("\n")
    if line[0] not in final:
        final[line[0]]={'Gateno':[line[2]],'Crossing_type':[line[1]],'Time':[line[3]]}
    else:
        for x,y in final.items():
            if x==line[0]:
                if line[1]=='ENTER' and y['Crossing_type'][len(y['Crossing_type'])-1]!='ENTER':
                    final[line[0]]['Gateno'].append(line[2])
                    final[line[0]]['Crossing_type'].append(line[1])
                    final[line[0]]['Time'].append(line[3])
                elif line[1]=='EXIT' and y['Crossing_type'][len(y['Crossing_type'])-1]!='EXIT':
                    final[line[0]]['Gateno'].append(line[2])
                    final[line[0]]['Crossing_type'].append(line[1])
                    final[line[0]]['Time'].append(line[3])
                elif line[1]=='EXIT' and y['Crossing_type'][len(y['Crossing_type'])-1]=='EXIT':
                    final[line[0]]['Gateno'][len(y['Crossing_type'])-1]=line[2]
                    final[line[0]]['Crossing_type'][len(y['Crossing_type'])-1]=line[1]
                    final[line[0]]['Time'][len(y['Crossing_type'])-1]=line[3]
# print(final)
option={'1':'Record of student','2':'get all the students between a time range','3':'get the number of times student entered through a gate'}
for x,y in option.items():
    print(int(x),':',y)
while True:
    n=input('Enter the option')
    if n=='':
        break
    else:
        if int(n)==1:
            ss=input('Enter the name')
            time=input('Enter the time')
            new_time=time.replace(':','')
            lss=[]
            for x,y in final.items():
                if ss==x:
                    for k in range(len(y['Time'])):
                        # newt=y['Time'][k].replace(':','')
                        # if newt<=new_time:
                        lss.append((y['Gateno'][k],y['Crossing_type'][k],y['Time'][k]))
            f2=open('option1.txt','w')
            f2.write(str(lss))
            f2.close()
            for x,y in final.items():
                if ss==x:
                    ltt=[]
                    for p in range((len(y['Crossing_type']))):
                        new=y['Time'][p].replace(':','')
                        ltt.append(new)
                    lt=[]    
                    for j in range(len(ltt)):
                        if ltt[j]<=new_time:
                            lt.append(y['Crossing_type'][j])  
                    if lt[len(lt)-1]=='ENTER':
                        print('On campus')
                    else:
                        print('Off campus')                                   
        elif int(n)==2:
            f3=open('option2.txt','w')
            start=input('Enter start time')
            new_start=start.replace(':','')
            print(new_start)
            end=input('Enter end time')
            new_end=end.replace(':','')
            print(new_end)
            entered=[]
            exit=[]
            for x,y in final.items():
                lk=[]
                for i in range(len(y['Time'])):
                    neww=y['Time'][i].replace(':','')
                    lk.append(neww)    
                for j in range(len(lk)):
                    if lk[j]>=new_start and lk[j]<=new_end and y['Crossing_type'][j]=='ENTER':
                        entered.append(x)
                        s=""
                        s=x+','+y['Crossing_type'][j]+','+y['Gateno'][j]+','+y['Time'][j]
                        f3.write(s)
                        f3.write('\n')
                    elif lk[j]>=new_start and lk[j]<=new_end and y['Crossing_type'][j]=='EXIT':
                        exit.append(x) 
                        s=""
                        s=x+','+y['Crossing_type'][j]+','+y['Gateno'][j]+','+y['Time'][j]
                        f3.write(s)
                        f3.write('\n')
            sentered=set(entered)
            sexit=set(exit)                  
            print('Entered',set(entered))
            print('Exit',set(exit))
            f3.close()              
        elif int(n)==3:
            gate=input('Enter gate number')
            count_enter=0
            count_exit=0
            for x,y in final.items():
                for i in range(len(y['Gateno'])):
                    if y['Gateno'][i]==gate and y['Crossing_type'][i]=='ENTER':
                        count_enter+=1
                    elif y['Gateno'][i]==gate and y['Crossing_type'][i]=='EXIT': 
                        count_exit+=1
            print('The no of time students entered:',count_enter) 
            print('The no. of times student exit:',count_exit)    
f.close()    