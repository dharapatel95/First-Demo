import json
fp=open('emp.json','r')
emp=json.load(fp)
print(emp)
for emps in emp:
    print(emps['name'])