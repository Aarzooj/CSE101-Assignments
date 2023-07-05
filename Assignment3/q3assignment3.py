import random
l=['File1.txt','File2.txt','File3.txt']
for i in range(len(l)):
    f=open(l[i],'r')
    s3=f.read()
    # print(s3)
    f.seek(0,0)
    s2=f.read()
    f.seek(0,0)
    s=f.read()
    s=s.split(' ')
    pp=',.;:'
    for j in range(len(s)):
        new=''
        s[j]=s[j].strip('\n')
        for k in s[j]:
            if k not in pp:
                new+=k
        s[j]=new    
        s[j]=s[j].rstrip('.')
        s[j]=s[j].rstrip(',') 
        s[j]=s[j].rstrip(';')
        s[j]=s[j].rstrip(':')
        s[j]=s[j].lower()    
    for k in s:
        if not k:
            s.remove(k)  
    # print(s)
    def F1(s):
        total_words=len(s)
        unique=[]
        for k in s:
            if k.lower() not in unique:
                unique.append(k)
        unique_words=len(unique)
        # return unique_words,total_words,unique
        return unique_words/total_words
    def F2(s):
        total_words=len(s)
        freq={}
        for i in s:
            if i.lower() not in freq:
                freq[i.lower()]=0
            freq[i.lower()]+=1
        new_freq=sorted([(y,x) for (x,y) in freq.items()])
        n_freq=new_freq[::-1]
        sum=0
        for h in range(5):
            sum+=int(n_freq[h][0])
        return sum/total_words
    def F5(s):
        if len(s)>750:
            return 1
        else:
            return 0
    def F3(s2):
        s2=s2.split('. ')
        l=[]
        for i in s2:
            if i!="":
                l.append(i) 
        l=[x for x in l if not all(c in '.,:;' for c in x)]              
        total_sentences=len(l)
        final_sentences=0
        for j in range(len(l)):
            l[j]=l[j].split(' ')
            for k in range(len(l[j])):
                l[j][k]=l[j][k].strip('\n')
                l[j][k]=l[j][k].strip(',')        
            for k in range(len(l[j])):
                if l[j][0]=='':
                    l[j].remove(l[j][0]) 
            for k in range(len(l[j])):
                if l[j][k]==',' or l[j][k]==';':
                    l[j].remove(l[j][k])                               
            if len(l[j])>35 or len(l[j])<5:
                final_sentences+=1        
        return final_sentences/total_sentences
    def F4(s3,s):
        total_words=len(s)
        lst=['.',',',':',';']
        i=0
        final=0
        count=1
        while i<=(len(s3)-2):
            if s3[i] in lst:
                if s3[i+1] in lst:
                    count+=1
                    i+=1
                elif s3[i+1] not in lst and count>1:
                    final+=1
                    i+=1 
                    count=1
                elif s3[i+1] not in lst and count==1:
                    i+=1
            else:
                i+=1
        return final/total_words 
    # print(F1(s))
    # print(F2(s))
    # print(F3(s2))
    # print(F4(s3,s))
    score=4+float(F1(s))*6+float(F2(s))*6-float(F3(s2))-float(F4(s3,s))-float(F5(s))
    print(score)
    f2=open('scores.txt','a')
    f2.write(l[i])
    f2.write('\n')
    ds='score'+':'+str(score)
    f2.write(ds)
    f2.write('\n')
    freq={}
    for i in s:
        if i.lower() not in freq:
            freq[i.lower()]=1
        freq[i.lower()]+=1
    new_freq=sorted([(y,x) for (x,y) in freq.items()])
    n_freq=new_freq[::-1]
    for j in range(5):
        f2.write(n_freq[j][1])
        f2.write(',')
    f2.write('\n')
    f2.write(str(random.choices(s,k=5)))
    f2.write('\n')  
    f2.close()   
    f.close()
    




