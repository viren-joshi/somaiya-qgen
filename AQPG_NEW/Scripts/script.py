import requests
import csv

module_mapper = {
    'Introduction to Database Concepts': 1,
    'Entity–Relationship Data Model':2,
    'Relational Model and Relational Algebra':3,
    'Structured Query Language (SQL)':4,
    'Relational-Database Design':5,
    'Transactions Management and Concurrency and Recovery':6
}

btlevel_mapper = {
    'Remember' : 1,
    'Understand' : 2,
    'Apply' : 3,
    'Analyze' : 4,
    'Evaluate' : 5,
    'Create' : 6
}




API_ENDPOINT = "http://127.0.0.1:8000/"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization" : "Token ab5edbdd05e4b302e0249e2d30f1f7f73a513515"
}


i=0
with open('data.csv', mode ='r', encoding="utf8") as file:

    csvFile = csv.reader(file)
    lines = 0
    for lines in csvFile:
        # print('l')
        # print(lines)
        # ['question', 'bt_level', 'paragraph', 'module', 'marks']
        # if i==516 or i==0:
        #     continue
        # print(lines[3].strip('.'))
        if lines[1] == 'Synthesis':
            x = 4
        else:
            x = btlevel_mapper[lines[1]]
        data = {
            "module_id" : module_mapper[lines[3].strip('.')],
            "question" : lines[0],
            "questionFile" : None,
            "answer" : lines[2],
            "marks" : lines[4],
            "BT_level" : x
        }
        print(data)
        i+=1

        # print(i)
        # if i==1:
        #     break

        if i>0 and i<517:
            r = requests.post(url = API_ENDPOINT, json = data, headers = headers)

        print(r)
        print("Response is: ", r.text)
