
import datetime 
import json
from urllib.request import urlopen
import sqlite3 as lite 
import pandas as pd 
import collections

cities = { "San Francisco": '37.727239,-123.032229',
"Seattle": '47.620499,-122.350876',
"Denver": '39.761850,-104.881105',
"Austin": '30.303936,-97.754355',
"Boston": '42.331960,-71.020173'
} 

key = '9118b46ef764b720fe448864eb41d727'

## Create SQL database 
con = lite.connect('weather.db')
cur = con.cursor()

# # Figure out all the types of data for each key 
# # for key in jData['currently']:
# # 	print(str(key) + str(type(key)))

cur.execute('DROP TABLE IF EXISTS weather;')
with con:
	# only use primary key if it is unique identifier
 	cur.execute('CREATE TABLE weather (city TEXT, time TEXT, temperature TEXT)')


# print("Response contains {0} properties".format(len(jData)))
# for key in jData:
#  	print(str(key) + " : " + str(jData[key]))

# jData['currently']['temperature'] --> where temp info is stored 


# Take each city and query every day for the past 30 days (Hint: You can use the datetime.timedelta(days=1) to increment the value by day)
with con: 

	for days in range(30): 
		# sets start date to 30 days before today 
		date = datetime.datetime.now() - datetime.timedelta(days=days)

		# convert to unix timestamp
		date = date.strftime("%s")
		date = str(date)

		for city in cities:
			URL = 'https://api.forecast.io/forecast/' + key + '/' + cities[city] + ',' + date

			response = urlopen(URL).read().decode('utf-8')
			jData = json.loads(response)

			time = jData['currently']['time']
			time = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
			temperature = jData['currently']['temperature']

			cur.execute('INSERT INTO weather VALUES (?,?,?)', (city, time, temperature))

# Save the max temperature values to the table, keyed on the date. You can leave the date in Unix time or convert to a string.




