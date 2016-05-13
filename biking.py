# Goal: Record number of bikes available every minute for an hour in NYC
# This will allow us to see which station is most active during that hour
# Activity = total number taken out OR returned 

import requests # requests is a URL handler to allow downloading from internet
from pandas.io.json import json_normalize 
import pandas as pd 
import matplotlib.pyplot as plt 

r = requests.get('http://www.citibikenyc.com/stations/json')

## Check out the data 

# print(r.json().keys()) # See the headers of the JSON blob

# print(r.json()['executionTime'])
# print(r.json()['stationBeanList'])

# print('Number of stations: % s' % len(r.json()['stationBeanList'])) # Get the number of stations


# ## Test that we have all fields by running through a loop
# key_list = [] #unique list of keys for each station
# for station in r.json()['stationBeanList']:
# 	for k in station.keys():
# 		if k not in key_list:
# 			key_list.append(k)

# print('Key list : % s' % key_list)

# ## convert into dataframe
df = json_normalize(r.json()['stationBeanList'])

print(df.head())
# print(df['statusValue'].unique())
# print(df.head())

# df['availableBikes'].hist()
# plt.show()

# Are there any test stations?
# print(any(df['testStation'] == True)) # shows that this does not contain any test stations
# print(df['testStation'][df['testStation'] == True].count()) # count how many test stations there are 

# # How many are in service or not? 
# print(df['statusValue'][df['statusValue'] == 'In Service'].count()) # count how many test stations there are 

# # Mean & median of bikes in a station 
# num_bikes_mean = df['availableBikes'].mean()
# num_bikes_med = df['availableBikes'].median()

# print('Median and mean of bikes available: {0}, {1}'.format(int(num_bikes_med), int(num_bikes_mean)))

# How does this change if we remove stations that aren't in service? 
# print(df['statusValue'].unique())

df['statusNew'] = df['statusValue'][df['statusValue'] == 'In Service'] # count how many test stations there are 
new_status = df['statusNew'].dropna() #need to not make new column type, weirdly 
# print(new_status)

num_bikes_mean = df.groupby(['statusValue'])['availableBikes'].mean()
num_bikes_med = df.groupby(['statusValue'])['availableBikes'].median()

# print(type(num_bikes_med), type(num_bikes_mean))
print(num_bikes_mean, num_bikes_med)
