import pandas as pd
import scipy.stats as stats
import numpy as np

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

# Splits data based on indication of new lines
data = data.split('\n')

# Then, split each item in this list on the commas; the bracketed expression 
# is a list comprehension. A list comprehension is a way of iterating 
# through the values of a list. 
data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1::] #all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

alc_mean = df['Alcohol'].mean()
alc_mean = float(alc_mean)
alc_med = df['Alcohol'].median()
# If all numbers occur equally often, stats.mode() will return the smallest number
alc_mode = stats.mode(df['Alcohol']) 
alc_mode = np.array(alc_mode, float)
alc_mode = float(alc_mode[0])

tob_mean = df['Tobacco'].mean() 
tob_mean = float(tob_mean)
tob_med = df['Tobacco'].median() 
tob_mode = stats.mode(df['Tobacco']) 
tob_mode = np.array(tob_mode, float)
tob_mode = float(tob_mode[0])


# See below for range, variance, SD
alc_range = max(df['Alcohol']) - min(df['Alcohol'])
alc_std = df['Alcohol'].std()
alc_variance = df['Alcohol'].var()

tob_range = max(df['Alcohol']) - min(df['Alcohol'])
tob_std = df['Alcohol'].std()
tob_variance = df['Alcohol'].var()

# "THE RANGE OF ALCOHOL AND TOBACCO IS: %s, %s" + alc_range, tob_range
#% means its a variable you'll read through, .2 is 2 decimal points
# print (The mean of the alcohol and tobacco is %.2f %.2f) % (alc_mean, tob_mean)


print("The range of Alcohol is: %.2f" % alc_range + '\n'
	"The range of Tobacco is: %.2f" % tob_range + '\n'
	"The median of Alcohol is: %.2f" % alc_med + '\n'
	"The median of Tobacco is: %.2f" % tob_med + '\n'
	"The mode of Alcohol is: %.2f" % alc_mode + '\n'
	"The mode of Tobacco is: %.2f" % tob_mode + '\n'
	"The mean of Alcohol is: %.2f" % alc_mean + '\n'
	"The mean of Tobacco is: %.2f" % tob_mean + '\n'
	"The standard deviation of Alcohol is: %.2f" % alc_std + '\n'
	"The standard deviation of Tobacco is: %.2f" % tob_std + '\n'
	"The variance of Alcohol is: %f" % float(alc_variance) + '\n'
	"The variance of Tobacco is: %f" % float(tob_variance)
	)

