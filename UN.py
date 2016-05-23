from bs4 import BeautifulSoup
import requests
import pandas as pd 
import sqlite3 as lite 

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

# print(soup.prettify())
# for row in soup('table'):
# 	print(row)
# print(soup.get_text()) # prints raw text 


table = soup('table')[6].find_all('tr')

Country = []
Year = []
Total = []
Men = []
Women = []

for i in range(8, 190):
	row = table[i]
	country = row.find_all('td')[0].string
	Country.append(country)

	year = row.find_all('td')[1].string
	Year.append(year)

	total = row.find_all('td')[4].string
	Total.append(total)

	men = row.find_all('td')[7].string
	Men.append(men)

	women = row.findAll('td')[10].string
	Women.append(women)
	
# print(Country, " ", Year, " ", Total, " ", Men, " ", Women)

df = pd.DataFrame(Country, columns=['Country'])
df['Year'] = Year
df['Total'] = Total
df['Men'] = Men
df['Women'] = Women 

# print(df.head())

# def df2sqlite(df, db_name = "GDP.db", tbl_name = "edu"):
 
#   conn=lite.connect(db_name)
#   cur = conn.cursor()                                 
 
#   wildcards = ','.join(['?'] * len(df.columns))              
#   data = [tuple(x) for x in df.values]
 
#   cur.execute("drop table if exists %s" % tbl_name)
 
#   col_str = '"' + '","'.join(df.columns) + '"'
#   cur.execute("create table %s (%s)" % (tbl_name, col_str))
 
#   cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)
 
#   conn.commit()
#   conn.close()


# df2sqlite(df, db_name="GDP.db", tbl_name)

data = df.items() #or itertuples()

con = lite.connect('GDP.db')

with con:
	cur = con.cursor()
	cur.execute('DROP TABLE IF EXISTS edu;')
	cur.execute('CREATE TABLE edu (Country, Year, Total, Men, Women);')
	wildcards = ','.join(['?'] * len(df.columns))
	data = [tuple(x) for x in df.values]
	cur.executemany('INSERT INTO %s VALUES(%s)' % ('edu', wildcards), data)


# df.to_sql(edu, con, flavor='sqlite', schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None)


# for i in df: 
# 	with con:
# 		cur.execute("INSERT INTO edu (Country, Year, Total, Men, Women) VALUES(?,?,?,?,?)", i[0], i[1], i[2], i[3], i[4])


