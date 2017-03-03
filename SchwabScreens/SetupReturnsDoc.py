import pandas as pd

file_name = 'Mar1_2/' + 'Screen6 Mar-01-2017'

df = pd.read_csv( file_name + '.csv')

#Sorting by a specific column
#Volume column has 4 spaces after
#df = df.sort_values('Volume    ')

symbols = list(df['Symbol'])
last_trades = list(df['Last Trade'])



text_file = open(file_name + "_RESULTS.txt", "w")
for i in range(len(symbols)):
    #symbols have extra whitespace that needs to be removed
    symbols[i] = symbols[i].strip()

    text_file.write(str(symbols[i]) + ' ' + str(round(last_trades[i],2)) + '\n')

text_file.close()
