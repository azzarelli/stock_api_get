import requests # API requesting
import datetime, time # time functionsality
import ast # dictionay functionality
import matplotlib.pyplot as plt 
import stock_func # own functions
import sys

import plotly.graph_objects as go # graphical
import chart_studio.tools as tls

# Time (Month ago) -------------------------------------------------------------------

Day = int(datetime.datetime.fromtimestamp(time.time()).strftime('%d'))
currentMonth = int(datetime.datetime.fromtimestamp(time.time()).strftime('%m'))
year = int(datetime.datetime.fromtimestamp(time.time()).strftime('%Y'))

if(currentMonth == 1):
    year = year - 1
    lastMonth = 12
else:
    lastMonth = currentMonth - 1

if((lastMonth == 2) and (DAY > 28)): # If last month Feb. and today is 29th,30th,31st than make last months day 28  
    prevDay = 28
elif((lastMonth == (5 or 7 or 10 or 11)) and (Day == 31)):# If last month has 30days and today is 31 then make last months day 30 
    prevDay = 30
else:
    prevDay = Day

lM_timeStamp = datetime.date(year, lastMonth, prevDay) # last Month time stamp
lM_unix = str(int(time.mktime(lM_timeStamp.timetuple())))

lY_timeStamp = datetime.date((year-1), currentMonth, prevDay)
lY_unix = str(int(time.mktime(lY_timeStamp.timetuple())))

curr_unix = str(int(time.time()))

# STOCK ------------------------------------------------------------------------
frontURL = 'https://finnhub.io/api/v1/'
endURL ='&token=br563avrh5r8ufep1f50'

#TYPE options: 'stock/profile', 'quote'
typeURL = 'quote'

ticker =  str(input("Ticker Name: "))
tickerURL = '?symbol=' + ticker

# Looking at types of Data recieved

data_time = str(input('Year or Month [Y/M]'))
if(data_time == 'Y'):
    stockCandleUrl = frontURL + 'stock/candle' + tickerURL + '&resolution=D&from='+ lY_unix + '&to='+ curr_unix + endURL
elif(data_time == 'M'):
    stockCandleUrl = frontURL + 'stock/candle' + tickerURL + '&resolution=D&from='+ lM_unix + '&to='+ curr_unix + endURL

currStockPriceURL = frontURL + 'quote' + tickerURL + endURL

stockCandleREQ = requests.get(stockCandleUrl)
currSPREQ = requests.get(currStockPriceURL)

stockCandle_fileCheck = str(stockCandleREQ.json())
currSP_fileCheck = str(currSPREQ.json())

stockCandleDATA = ast.literal_eval(stockCandle_fileCheck)
currSPDATA = ast.literal_eval(currSP_fileCheck)

# Checks if the ticker Exists

stock_func.fileCheck(stockCandle_fileCheck, stockCandleDATA, currSP_fileCheck, currSPDATA)

# Plotting Candle Data

closeCandlePrice = stockCandleDATA['c'[0]]
currStockPrice = currSPDATA['c']

y = stock_func.makeAxis_x(len(closeCandlePrice))

# Plotly

fig = go.Figure()
fig.add_trace(go.Scatter(x=y, y=closeCandlePrice,
                    mode='lines',
                    name='closingStockPrice'))
fig.show()


