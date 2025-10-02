import json
f=open('emp1.json','r')
emp=json.load(f)
for emps in emp:
    if emps['gender'] == 'Female':
        print("Employee ID: ",emps['empid'], "Name: ",emps['name'])