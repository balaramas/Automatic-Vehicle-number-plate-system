import requests
import json
import csv
#Use your api url from any sms sending service available to you.
URL = 'https://www.sms4india.com/api/v1/sendCampaign'
text=""
f=open("data/images/number.txt", "r")
if f.mode == 'r':
  contents =f.read()
  text=contents

file = open('drivers.csv', 'rb')
reader=csv.reader(file)
headers=next(reader, None)
username=''
vehicle=''
phno=''
column={}
for h in headers:
  column[h]=[]
for row in reader:
  for h, v in zip(headers, row):
    column[h].append(v)

var=-1

for i in column['License_Number']:
  var=var+1
  if text==i:
    phno=column['Phone'][var]
    username=column['Car_Owner'][var]
    vehicle=column['Vehicle'][var]
    

print phno
print username
print vehicle

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


response = sendPostRequest(URL, 'PLZ7516MF6QXW6FGYM148XI5BYVLZZVZ', 'C5N08S454QGXZR0M', 'stage', phno , 'SPD-TKT', 'Dear '+username+' You have been charged with speeding ticket. Fine amount Rs 100 for vehicle '+vehicle+' License Number - '+text+'. Please submit the amount at nearest traffic stop to avoid further penalty!' )

print response.text
#print var
