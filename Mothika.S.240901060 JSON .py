#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Open a text file in Write mode
f=open("D:/textfile.txt",'w')
f.write("first line\n")
f.write("second line\n")
f.write("third line\n")
#Open a text file in Read mode
k=open("D:/textfile.txt",'r')
print(k.readline())
print(k.readline())
print(k.readline())
k.close()
#open a text file in Append mode
m=open("D:/textfile.txt",'a')
m.write("fourth line\n")
m.write("fifth line\n")
m.close()
#Open a text file in Read mode
p=open("D:/textfile.txt",'r')
print(p.read())
p.close()
with open("D:/textfile.txt",'r')as file:
    lines=file.readlines()
    print(lines)
import json
#JSON string
x='{"name":"John","age":30,"city":"New York"}'
y=json.loads(x)
print(y["age"])
#Python dictionary
data={
    "name":"John",
    "age":30,
    "city":"New York"
}
json_data=json.dumps(data)
print(json_data)

