import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import _candlestick
import matplotlib
matplotlib.rcParams.update({'font.size': 9})

eachStock = 'TSLA', 'AAPL'

def graphData(stock):
    try:
        stockFile = stock +'.txt'
        
        date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',', unpack=True,
                         converters={0: mdates.strpdate2num('%Y%m%d')})

        x = 0
        y = len(date)
        candleAr = []
        while x < y:
            appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
            candleAr.append(appendLine)
            x += 1

        
    
        fig = plt.figure(facecolor='#07000d')
        ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4, axisbg='#07000d')
        _candlestick(ax1, candleAr, width=1, colorup='#9eff15', colordown='#ff1717')
        ax1.grid(True, color='w')
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
        ax1.yaxis.label.set_color("w")
        ax1.spines['bottom'].set_color("#5998ff")
        ax1.spines['top'].set_color("#5998ff")
        ax1.spines['left'].set_color("#5998ff")
        ax1.spines['right'].set_color("#5998ff")
        ax1.tick_params(axis='y', colors='w')
        plt.ylabel('Stock price')

        volumeMin = volume.min()
        

        ax2 = plt.subplot2grid((5,4), (4,0), sharex=ax1, rowspan=1, colspan=4, axisbg='#07000d')
        ax2.plot(date, volume, '#00ffe8', linewidth=.8)
        ax2.fill_between(date, volumeMin, volume, facecolor='#00ffe8', alpha=.5)
        ax2.axes.yaxis.set_ticklabels([])
        plt.ylabel('Volume')
        ax2.grid(False)
        ax2.spines['bottom'].set_color("#5998ff")
        ax2.spines['top'].set_color("#5998ff")
        ax2.spines['left'].set_color("#5998ff")
        ax2.spines['right'].set_color("#5998ff")
        ax2.tick_params(axis='x', colors='w')
        ax2.tick_params(axis='y', colors='w')


        plt.ylabel('Volume', color=  'w')      
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(90)

        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        plt.suptitle(stock+' Stock Price', color='w')


        plt.setp(ax1.get_xticklabels(), visible=False)
        plt.subplots_adjust(left=.09, bottom=.14, right=.94, top=.95, wspace=.20, hspace=0)

        plt.show()
        fig.savefig('example.png',facecolor=fig.get_facecolor())
        
    except Exception, e:
        print 'failed main loop', str(e)

for stock in eachStock:
    graphData(stock)


