import pandas as pd 
import collections 
import requests
from dateutil.parser import parse 

con = lite.connect('citi_bike.db')
cur = con.cursor()

df = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time",con,index_col='execution_time')

# Need to figure out how to subtract raw data from previous data to store just the activity value 
activity_sum = collections.defaultdict(int)

for col in df.columns:
	station_vals = df[col].tolist()
	station_change = 0
	for k, v in enumerate(station_vals):
		if k < len(station_vals) - 1:
			station_change += abs(station_vals[k] - station_vals[k+1])
	hour_change[int(station_id)] = station_change

# Should we try to add this to a new counter column? 


def keywithmaxval(d):
	"""Find key with greatest value"""
	return max(d, key=lambda k: d[k])

max_station = keywithmaxval(hour_change)

