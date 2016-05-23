import csv
import sqlite3 as lite

con = lite.connect('GDP.db')

with con:
	cur = con.cursor() 

	cur.execute('DROP TABLE IF EXISTS gdp;')
	cur.execute('CREATE TABLE gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010);')


with open('GDP.csv', newline='', encoding='iso-8859-1') as f:
	reader = csv.reader(f)
	for line in reader:
		with con:
			cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[42:-6]) + '");')
