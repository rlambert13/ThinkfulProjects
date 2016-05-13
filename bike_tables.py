
import sqlite3 as lite
import requests # requests is a URL handler to allow downloading from internet
from pandas.io.json import json_normalize 
import pandas as pd 
import matplotlib.pyplot as plt 
import time #has datetime objects
from dateutil.parser import parse # parse string into date time object
import collections 
import time
import apscheduler.scheduler import Scheduler #allows you to schedule jobs

r = requests.get('http://www.citibikenyc.com/stations/json')
df = json_normalize(r.json()['stationBeanList'])

con = lite.connect('citi_bike.db')
cur = con.cursor()

## First create the static identifying information table 
with con: 
	cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT)')

sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

# populate values into the database
with con:
	for station in r.json()['stationBeanList']:
		cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))


## Create the available bikes dynamic data

# First, need to ensure column name starts with a string identifier
station_ids = df['id'].tolist()
station_ids = ['_' + str(x) + ' INT' for x in station_ids]

with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")


# parse string into datetime object
exec_time = parse(r.json()['executionTime'])

with con:
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))

# Start the scheduler
sched = Scheduler()
sched.start()

def job_function(): 
	# Iterate through stations
	id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

	for station in r.json()['stationBeanList']:
		id_bikes[station['id']] = station['availableBikes']

	# Iteration through the defaultdict to update values in the database
	# strftime() -- formats the time 
	with con: 
		for k, v in id_bikes.iteritems():
			cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")

	time.sleep(1)

# Schedules job to be run once each minute
sched.add_cron_job(job_function, minute='0-59')









