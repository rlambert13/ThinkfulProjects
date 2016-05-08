import matplotlib.pyplot as plt 
import pandas as pd 
import scipy.stats as stats

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# Remove rows with null values
loansData.dropna(inplace=True)


## Looks at Amount Requested

loansData.boxplot(column='Amount.Requested')
plt.show()
plt.savefig("RequestedBox.png")

loansData.hist(column='Amount.Requested')
plt.show()
plt.savefig("RequestedHist.png")

plt.figure()
graph1 = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()
plt.savefig("RequestedQQ.png")


## Looks at Amount Funded by Investors 

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

# Does the loan amounts look normally distributed?
plt.figure()
graph2 = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()

