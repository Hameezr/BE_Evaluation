import json

birthdayData = json.loads(open('birthday.json').read())
print('Here\'s birthday catalogue for Carteblanche')

for key in birthdayData.keys():
    print(key)

data = (input("Enter name and their birthday after colon in the format dd/mm/yyyy: e.g Hameez Rizwan:29/10/1997 -> ").split(':'))
birthdayData.update({data[0]: data[1]})

file = open('birthday.json', 'w')
birthdayData = json.dumps(birthdayData)
file.write(birthdayData)
file.close()

print(data[0], 'added to the dict, here\'s the updated list')
birthdayData=json.loads(birthdayData)
for key in birthdayData.keys():
    print(key)