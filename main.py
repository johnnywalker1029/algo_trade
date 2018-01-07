from lib.data_generator import DataGenerator as dg
import datetime

freq = 'D'
start = datetime.date(2017,1,1)
end = datetime.date(2017,12,31)
hoildays = ['20171231','20170101']
price = 21
range = 0.3

dg.gen(freq,start,end,hoildays,price,range)