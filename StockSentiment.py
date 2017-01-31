from datetime import date
import pandas as pd

#Idea is to calculate the percentage rise from earnings
#Facebook reports on Wednesday February 1 after the close.
#Price change will be Thursday opening price minus
#Wednesday closing 

#symbol -> earnings date
stocks = {'FB':[date(2017, 2, 1)],
            'SHOP':[date(2017, 2, 15)],
            'NOW':[date(2017, 1, 25)]
}

past_stocks = {'FB':[(date(2016, 11, 2), 5.7), (date(2016, 7, 27), 4.5), 
                    (date(2016, 4, 27), 3.4), (date(2016, 1, 27), 4.8)],
            'SHOP':[date(2017, 2, 15)],
            'NOW':[date(2017, 1, 25)]
}



xl = pd.ExcelFile('Q4_2016/' + 'IBD.xls')
print(xl.sheet_names)

df = xl.parse('Stock list', skiprows=8)
my_stocks = []
for index, row in df.iterrows():
    my_stocks.append( (row['Symbol'], row['Earnings Date']))

#sorted by earnings date
for i in sorted(my_stocks, key=lambda earnings: earnings[1]):
    print (i)
    

