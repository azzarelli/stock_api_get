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
ticker = 'IBM' # str(input("Ticker Name: "))
tickerURL = '?symbol=' + ticker

data_time = 'Y' #str(input('View DATA over last Year or Month [Y/M]'))

q_compare = int(input('How many are you comparing? '))
other_tickers = str(input('Enter Ticker Names: '))
ot = other_tickers.split(',')
if q_compare != len(ot):sys.exit()
ot.insert(0, ticker)
print(ot)

url_cand, url_price = sf.glueURL(ot, lY_unix, lM_unix, curr_unix, data_time)
tick_data_cand = []
tick_data_price = []

for i in range(len(ot)):
    stockCandleUrl = url_cand[i]
    currStockPriceURL = url_price[i]
    
    stockCandleREQ = requests.get(stockCandleUrl)
    currSPREQ = requests.get(currStockPriceURL)

    stockCandle_fileCheck = str(stockCandleREQ.json())
    currSP_fileCheck = str(currSPREQ.json())

    stockCandleDATA = ast.literal_eval(stockCandle_fileCheck)
    currSPDATA = ast.literal_eval(currSP_fileCheck)

    # Checks if the ticker Exists
    sf.fileCheck(stockCandle_fileCheck, stockCandleDATA, currSP_fileCheck, currSPDATA)

    # Plotting Candle Data

    tick_data_cand.append(stockCandleDATA['c'[0]])
    timeStamp = 0
    tick_data_price.append(currSPDATA['c'])

x_axis = [datetime.datetime.utcfromtimestamp(stockCandleDATA['t'[0]][i]).strftime('%Y-%m-%d') for i in range(len(tick_data_cand[0]))]

# Plotly
fig = go.Figure()
for i in range(len(tick_data_cand)):
    fig.add_trace(go.Scatter(x=x_axis, y=tick_data_cand[i],
                        mode='lines',
                        name=ot[i]))
fig.show()


