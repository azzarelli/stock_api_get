 # stock_api.py function are located here
import datetime, time # time functionsality

# file check - if any data is not returned from get then ...
def fileCheck(sc_fc, sc_data, sp_fc, sp_data):
     if((str(sc_fc) == "{}") or (sc_data == 'no_data' )):
        sys.exit('Stock Candles Data Not Found')
     if((str(sp_fc) == "{}") or (sp_data == 'no_data' )):
        sys.exit('Current Stock Price Data Not Found')

def makeAxis_x(length):
     y = [0]
     for x in range(1, length):
          y.append(x)
     return y

# Get date/time
def getdate():
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
     elif((lastMonth == (4 or 7 or 10 or 11)) or (Day == 31)):# If last month has 30days and today is 31 then make last months day 30 
         prevDay = 30
     else:
         prevDay = Day
     print(prevDay, lastMonth, year)

     lM_timeStamp = datetime.date(year, lastMonth, prevDay) # last Month time stamp
     lM_unix = str(int(time.mktime(lM_timeStamp.timetuple())))

     lY_timeStamp = datetime.date((year-1), currentMonth, prevDay)
     lY_unix = str(int(time.mktime(lY_timeStamp.timetuple())))

     curr_unix = str(int(time.time()))
     return lM_timeStamp,lM_unix,lY_timeStamp,lY_unix,curr_unix, prevDay, lastMonth, year

# Glue url for API fetch process
def glueURL(tickerURL, lY_unix,lM_unix, curr_unix, data_time):
     frontURL = 'https://finnhub.io/api/v1/'
     endURL ='&token=br563avrh5r8ufep1f50'
     if(data_time == 'Y'):
         stockCandleUrl = frontURL + 'stock/candle' + tickerURL + '&resolution=D&from='+ lY_unix + '&to='+ curr_unix + endURL
     elif(data_time == 'M'):
         stockCandleUrl = frontURL + 'stock/candle' + tickerURL + '&resolution=D&from='+ lM_unix + '&to='+ curr_unix + endURL

     currStockPriceURL = frontURL + 'quote' + tickerURL + endURL
     return stockCandleUrl, currStockPriceURL
