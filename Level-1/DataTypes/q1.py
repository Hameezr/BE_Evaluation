import json

birthdayData = json.loads(open('birthday.json').read())

print('Here\'s birthday catalogue for Carteblanche')
for key in birthdayData.keys():
    print(key)
name = input('who\'s birthday do you wanna know?\n')
if name in birthdayData:
    print(name, 'birthday is at', birthdayData[name])
else:
    print(str(name) + ' does not exist')