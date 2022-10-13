import json

users = []

data = {
        "users":[
              
        ],

        "score":[

        ],

}



y = json.dumps(data,indent=4)

print(y)

f = open('user.json','w')
f.write(y)
f.close()

abdul = {
    'name':'Abdulrahman',
    'age':23,
    'level':100
}

malik = {
    'name':'malik',
    'age':20,
    'level':100
}
sandra = {
    'name':'sandra',
    'age':30,
    'level':100
}

f = open('user.json','r')
x = f.read()
f.close()

x = json.loads(x)

print(x)

x['users'].append(abdul)
x['users'].append(malik)
x['users'].append(sandra)


print(x)

x = json.dumps(x)

f = open('user.json','w')



