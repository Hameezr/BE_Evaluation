from calendar import month
import json

birthdayData = json.loads(open('birthday.json').read())
months = json.loads(open('months.json').read())

countArr = [0]*12

for val in birthdayData.values():
    countArr[int((val.split('/')[1]))-1]+=1

for count in range(0, len(countArr)):
    print (months.get(str(count)), countArr[count])
