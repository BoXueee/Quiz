import requests
import json
import getpass

username = raw_input('Please input user name: \n')
password = getpass.getpass('Please input password: \n')

r1 = requests.put("https://boxue.cloudant.com/boxue_testdb",
             auth=(username, password))

if r1.status_code == 201:
   print 'Create database boxue_testdb succeeded.'
elif r1.status_code == 412:
   print 'Database boxue_testdb already exist.'
elif r1.status_code == 401:
   print 'Incorrect credential.'
   quit()         		 
else:
   print 'Error occurred while creating database, rc =', r1.status_code
			 
r2 = requests.put("https://boxue.cloudant.com/boxue_testdb/boxue_testdoc",
             auth=(username, password),
             headers={"content-type":"application/json"},
             data=json.dumps({"foo":"bar"}))	
			 
if r2.status_code == 201:
   print 'Create document boxue_testdoc succeeded.'
elif r2.status_code == 409:
   print 'Document boxue_testdoc already exist.'
else:   
   print 'Error occurred while creating document, rc =', r2.status_code		 

r3 = requests.get("https://boxue.cloudant.com/boxue_testdb/boxue_testdoc",
             auth=(username, password))		

if r3.status_code == 200:
   print 'Get document boxue_testdoc succeeded.' 
   print 'headers: ', r3.headers['content-type']
   print 'encoding: ', r3.encoding
   print 'text: ', r3.text 
   print 'json: ', r3.json()
else:
   print 'Error occurred while retrieving document boxue_testdoc, rc =', r3.status_code		   
