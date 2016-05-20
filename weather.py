
import datetime 
import json
import requests
from urllib.request import urlopen
import sqlite3 as lite 
import pandas as pd 
from sqlalchemy import create_engine # database connection
import collections
import matplotlib as plt 

cities = { "San Francisco": '37.727239,-123.032229',
"Seattle": '47.620499,-122.350876',
"Denver": '39.761850,-104.881105',
"Austin": '30.303936,-97.754355',
"Boston": '42.331960,-71.020173'
} 

api_key = '9118b46ef764b720fe448864eb41d727'
url = 'https://api.forecast.io/forecast/' + api_key

## Create SQL database 
con = lite.connect('weather.db')
cur = con.cursor()

end_date = datetime.datetime.now() 

cities.keys()

cur.execute('DROP TABLE IF EXISTS daily_temp;')

with con:
    cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, city1 REAL, city2 REAL, city3 REAL, city4 REAL, city5 REAL);')

query_date = end_date - datetime.timedelta(days=30) #the current value being processed

with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)

for k,v in cities.items():
    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
    while query_date < end_date:
        #query for the value
        r = requests.get(url + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))

        with con:
            #insert the temperature max to the database
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))

        #increment query_date to the next day for next operation of loop
        query_date += datetime.timedelta(days=1) #increment query_date to the next day


con.close() # a good practice to close connection to database

## Start the plotting exercises

# Use create engine plugin to initialize the database and then read sql into a dataframe 
disk_engine = create_engine('sqlite:///weather.db') # Initializes database with filename 311_8M.db in current directory

df = pd.read_sql_query('SELECT temperature as temp, time as day FROM weather WHERE city = "Boston" ORDER BY time ASC', disk_engine)
print(df.head())

# x = plt.date2num(df.day)
# x = plt.dates.date2num(df.day)
# y = df.temp.astype(float)

# plt.figure()
# plt.plot(x, y)
# plt.show()
