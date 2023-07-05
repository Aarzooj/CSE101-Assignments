list=['abuse','anger','apple','youth','beach','block','cause','chain','chest','dance','death','doubt','drama','earth','enemy','error','faith','field','floor','focus','glass','grant','guide','heart','horse','image','index','japan','jones','judge','knife','laura','layer','level','limit','lunch','major','metal','model','night','noise','offer','panel','peace','pilot','queen','radio','reply','river','scope','sheep','table','uncle','visit','woman','world']
import random
n=random.randint(0,len(list)-1)
word=list[n]
# print(word)

count=0
while True:
    count+=1
    print('the number of the guess',count)
    x=input('Enter')
    if x==word:
        print("Guess is correct")
        break
    else:
        if  count<6:
            final=[]
            l=[]                        
            for j in range(len(word)):
                if word[j]==x[j]:                
                    print(x[j],end="")
                    final.append(x[j])
                else:
                    print('-',end="")    
            print()
            for i in x:
                if i in word and i not in final:
                    l.append(i)           
            print('other characters present')
            if set(l)!=set():                           
                print(set(l)) 
            else:
                print(" ")                
        else:
            print("Sorry couldnot guess")
            break


