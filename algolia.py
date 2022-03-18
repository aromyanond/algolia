import json

with open('algolia.json', 'r',encoding='UTF-8', errors='ignore') as f:
  data = json.load(f)

for user in data['users']:
  print (user['email'])
  del(user['gender'], user ['phone_number'], user['birthdate'], 
  user['location'], user['username'], user['password'], 
  user['first_name'], user['last_name'], user['title'], user['picture'])


with open('user_email.json', 'w') as f:
  json.dump(data, f, indent=2)

