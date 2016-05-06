import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats
import collections 


## Box Plot
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

plt.boxplot(x)
plt.show()
plt.savefig("boxplot.png")


## Histogram 
plt.hist(x, histtype='bar')
plt.show()
plt.savefig("histogram.png")


## Frequencies
testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

# calculate frequency of numbers in a list -- which is sum of that number * instances / sum of all values
# first find sum of all values as denominator
count_sum = sum(c.values())

for k,v in c.items():
	print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))


## QQ Plot 
plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.savefig("QQPlot1.png")

plt.figure()
test_data2 = np.random.uniform(size=1000)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph
plt.savefig("QQPlot2.png")