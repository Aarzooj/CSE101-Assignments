import requests 
base_url="https://od-api.oxforddictionaries.com/api/v2"
app_id="08d33fd0"
api_key="8d60f6727145703897c4f397165271ae"

language="en-gb"
#url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
#resp=requests.get(url, headers={"app_id": app_id, "app_key": api_key})
#data=resp.json()
list=['abuse','anger','apple','youth','beach','block','cause','chain','chest','dance','death','doubt','drama','earth','enemy','error','faith','field','floor','focus','glass','grant','guide','heart','horse','image','index','japan','jones','judge','knife','laura','layer','level','limit','lunch','major','metal','model','night','noise','offer','panel','peace','pilot','queen','radio','reply','river','scope','sheep','table','uncle','visit','woman','world']
import random
n=random.randint(0,len(list)-1)
word=list[n]
print(word)
count=0
while True:
    word_id=input("Enter a word")
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    resp=requests.get(url, headers={"app_id": app_id, "app_key": api_key})
    if resp.status_code==200:  
        count+=1 
        print('the number of the guess',count)
        print("Valid word entered!")
        if word_id==word:
            print("Guess is correct")
            break
        else:
            if count<6:
                final=[]
                l=[]                        
                for j in range(len(word)):
                    if word[j]==word_id[j]:                
                        print(word_id[j],end="")
                        final.append(word_id[j])
                    else:
                        print('-',end="")    
                print()
                for i in word_id:
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
            
    else:
        print("Not a valid word")  
        pass




