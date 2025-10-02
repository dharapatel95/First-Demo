import json

emp_json = '''
[
    {"id":101,"name":"Rahul","salary":20000},
    {"id":102,"name":"Sonia","salary":30000},
    {"id":103,"name":"Priya","salary":40000}
]
'''

employees = json.loads(emp_json)   # use loads for string

print(type(employees))  # should print <class 'list'>
print(employees)

for emp in employees:
    print(emp['name'])
