

import sqlite3 as lite
import requests # requests is a URL handler to allow downloading from internet
from pandas.io.json import json_normalize 
import pandas as pd 
import matplotlib.pyplot as plt 
import time #has datetime objects
from dateutil.parser import parse # parse string into date time object
import collections 
import time

con = lite.connect('citi_bike.db')
cur = con.cursor()

# Remove tables if they already exist 
cur.execute('DROP TABLE IF EXISTS citibike_reference;')
cur.execute('DROP TABLE IF EXISTS available_bikes;')

## First create the static identifying information table 
with con: 
	cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT)')
	# cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")
	cur.execute('CREATE TABLE available_bikes (execution_time DATETIME, station_ids INT, num_available INT)')

for i in range(60):
	r = requests.get('http://www.citibikenyc.com/stations/json')
		# df = json_normalize(r.json()['stationBeanList'])

		# # First, need to ensure column name starts with a string identifier
		# station_ids = df['id'].tolist()
		# station_ids = ['_' + str(x) + ' INT' for x in station_ids]

	sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
	sqltwo = "INSERT INTO available_bikes (execution_time, station_ids, num_available) VALUES (?,?,?)"

		# populate values into the database
	with con:

			# Iterate through stations
		id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

		# Parse string into datetime object
		exec_time = parse(r.json()['executionTime'])

		for station in r.json()['stationBeanList']:
			if i == 0:
				cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],
					station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],
					station['landMark'],station['latitude'],station['location']))	
				
			id_bikes[station['id']] = station['availableBikes']	

			# Iteration through the defaultdict to update values in the database
			for k, v in id_bikes.items():
				cur.execute(sqltwo,(exec_time, int(k), int(v)))


	time.sleep(60) # sleep every minute / pause program for this many seconds


	







