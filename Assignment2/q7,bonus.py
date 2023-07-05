#merged dictionary with Anushka Shrivastava(2022086)
import json
with open('aarzoo.json') as f:
    addrbook1=json.load(f)   #will give as a dictionary
    
with open('anushka.json') as f:
    addrbook2=json.load(f) 
final_json={}     
file1=addrbook1['Address Book']   
file2=addrbook2['Address Book']   
for x,y in file1.items():
    for a,b in file2.items():
        if x==a:
            if y!=b:
                y.append(b)            
file2.update(file1)
final_json["Address Book"]=file2
print(json.dumps(final_json,indent=4)) # to convert into final dictionary

with open('merged.json','w') as f:
    f.write(json.dumps(final_json,indent=4))
