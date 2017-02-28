import pandas as pd

large_cap_df = pd.read_csv('Small Cap Only With P-E Feb-28-2017.csv')
symbols = list(large_cap_df['Symbol'])
last_trades = list(large_cap_df['Last Trade'])


text_file = open("Small Cap Only With P-E Feb-28-2017" + "_RESULTS.txt", "w")
for i in range(len(symbols)):
    #symbols have extra whitespace that needs to be removed
    symbols[i] = symbols[i].strip()

    text_file.write(str(symbols[i]) + ' ' + str(last_trades[i]) + '\n')

text_file.close()


    
