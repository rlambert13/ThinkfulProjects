import pandas as pd 
import numpy as np 

## Weather
# df = pd.DataFrame({'rainy': [.4, .7], 'sunny': [.6, .3]}, 
# 	index=["rainy", "sunny"])

# print(df.dot(df))

## Markets
df = pd.DataFrame({'Bull Market': [.9, .8, .5],
	'Bear Market': [.25, .05, .25],
	'Stagnant Market': [.75, .15, .25]
	}, index = ["Bull Market", "Bear Market", "Stagnant Market"])

def find_state_after_n(df, n):
	multiply = np.linalg.matrix_power(df, n)
	state = np.dot(df, multiply)
	return state 

p = find_state_after_n(df, 4)
print (p)