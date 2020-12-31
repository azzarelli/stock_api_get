import requests # API requesting
import datetime, time # time functionsality
import ast # dictionay functionality
import matplotlib.pyplot as plt 
import sys
import plotly.graph_objects as go # graphical

import stock_func as sf
# Time (Month ago) -------------------------------------------------------------------

lM_timeStamp,lM_unix,lY_timeStamp,lY_unix,curr_unix, D,M,Y = sf.getdate()

# STOCK ------------------------------------------------------------------------

#TYPE options: 'stock/profile', 'quote'
typeURL = 'quote'
ticker = str(input("Ticker Name: "))
tickerURL = '?symbol=' + ticker

data_time = str(input('View DATA over last Year or Month [Y/M]'))

stockCandleUrl, currStockPriceURL = sf.glueURL(tickerURL, lY_unix, lM_unix, curr_unix, data_time)

stockCandleREQ = requests.get(stockCandleUrl)
currSPREQ = requests.get(currStockPriceURL)

stockCandle_fileCheck = str(stockCandleREQ.json())
currSP_fileCheck = str(currSPREQ.json())

stockCandleDATA = ast.literal_eval(stockCandle_fileCheck)
currSPDATA = ast.literal_eval(currSP_fileCheck)

# Checks if the ticker Exists
sf.fileCheck(stockCandle_fileCheck, stockCandleDATA, currSP_fileCheck, currSPDATA)

# Plotting Candle Data

closeCandlePrice = stockCandleDATA['c'[0]]
timeStamp = 0
currStockPrice = currSPDATA['c']

x_axis = [datetime.datetime.utcfromtimestamp(stockCandleDATA['t'[0]][i]).strftime('%Y-%m-%d') for i in range(len(closeCandlePrice))]

# Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_axis, y=closeCandlePrice,
                    mode='lines',
                    name='closingStockPrice'))
fig.show()


