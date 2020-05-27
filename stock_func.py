 # stock_api.py function are located here

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
