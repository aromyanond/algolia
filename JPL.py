import json

with open('algolia.json', encoding="utf-8") as f:
    data=json.load(f)

for users in data['users']:
    print (users['email'])
    del (users['gender'], users['phone_number'], 
    users['birthdate'],users['location'],users['username'],
    users ['password'], users['first_name'], users ['last_name'],
    users['title'],users['picture'])


json_object=json.dumps(data, indent=2, ensure_ascii=False)

    
with open('email_list.json', 'w', encoding="utf-8") as f:
    f.write(json_object)
   
