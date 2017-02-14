import urllib2
import time
import datetime

stocksToPull = 'AAPL','MSFT','CMG','AMZN','EBAY','TSLA'

def pullData(stock):
    try:
        print 'Currently pulling',stock
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=3y/csv'
        saveFileLine = stock+'.txt'

        try:
            readExistingData = open(saveFileLine,'r').read()
            splitExisting = readExistingData.split('\n')
            mostRecentLine = splitExisting[-2]
            lastUnix = mostRecentLine.split(',')[0]
        except Exception:
            lastUnix = 0

        saveFile = open(saveFileLine,'a')
        sourceCode  = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
        
        for eachLine in splitSource:
            if 'values' not in eachLine:
                splitLine = eachLine.split(',')
                if len(splitLine) == 6:
                    if splitLine[0] > lastUnix:
                        lineToWrite = eachLine+'\n'
                        saveFile.write(lineToWrite)

        saveFile.close()

        print 'Pulled', stock
        print 'sleeping....'
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)

            
    
    except Exception, e:
        print 'main loop', str(e)

for eachStock in stocksToPull:
    pullData(eachStock)
