import pandas as pd
import numpy as np
import random as rand

from datetime import timedelta, date

class DataGenerator:

	columns = {'trade_date','price','high','low','mkt_vol','adjusted_price'}

	@staticmethod
	def genYearly(start,end,hoildays,price,range):
		print('gen yearly')
	
	def genMonthly(start,end,hoildays):
		print('gen Monthly')	
	
	@staticmethod
	def genDaily(start,end,hoildays,price,range):
		print('gen Daily')
		for date in DataGenerator.date_range(start,end,hoildays):
			price = price + rand.uniform(-1,1)*range
			print(''+price)
	
	def genHourly(start,end,hoildays):
		print('Not Implemented Yet.')	
	
	def genMinutes(start,end,hoildays):
		print('Not Implemented Yet.')	
	
	def genSeconds(start,end,hoildays):
		print('Not Implemented Yet.')

	@staticmethod
	def date_range(start, end,hoildays):
		for n in range(int ((end - start).days)+1):
			date = start + timedelta(n)
			if date.weekday() != 5 and date.weekday() != 6 and date not in hoildays:
				yield start + timedelta(n)

	#freq: 'Y','M','D','H','M','S'
	#start: start date
	#end: end date
	#hoildays: hoildays
	@staticmethod
	def gen(freq,start,end,hoildays,price,range):
		if freq == 'Y':
			DataGenerator.genYearly(start,end,hoildays,price,range)
		elif freq == 'M':
			genMonthly(start,end,hoildays)
		elif freq == 'D':
			DataGenerator.genDaily(start,end,hoildays,price,range)
		elif freq == 'H':
			genHourly(start,end,hoildays)
		elif freq == 'MIN':
			genMinutes(start,end,hoildays)
		elif freq == 'S':
			genSeconds(start,end,hoildays)