import json

data = '{"name": "mark", "mail": "mark@mail.com", "phone_number": 911, "subject": ["history", "chemistry"]}'

y = json.loads(data)

print(y["name"])