import pandas as pd

file_name = 'Mar2_3/' + 'WeakGainers Mar-02-2017'

large_cap_df = pd.read_csv( file_name + '.csv')
symbols = list(large_cap_df['Symbol'])
last_trades = list(large_cap_df['Last Trade'])


text_file = open(file_name + "_RESULTS.txt", "w")
for i in range(len(symbols)):
    #symbols have extra whitespace that needs to be removed
    symbols[i] = symbols[i].strip()

    text_file.write(str(symbols[i]) + ' ' + str(round(last_trades[i],2)) + '\n')

text_file.close()
