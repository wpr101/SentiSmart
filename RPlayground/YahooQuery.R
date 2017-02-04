base <- "http://query.yahooapis.com/v1/public/yql?"
begQuery <- "q=select * from yahoo.finance.historicaldata where symbol in "
midQuery <- "( 'YHOO', 'GOOGL') "
endQuery <- "and startDate = '2014-01-01' and endDate = '2014-12-31'"
endParams <- "&diagnostics=true&env=store://datatables.org/alltableswithkeys"

urlstr <- paste0(base, begQuery, midQuery, endQuery, endParams)
print(urlstr)
