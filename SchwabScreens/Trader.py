import pandas as pd
import os
import operator

file_name = 'TRADING Mar-21-2017.csv'
path = 'Mar21_22/'
column_match = {}

df = pd.read_csv( os.path.join(path, file_name))

columns_list = list(df.columns.values)

#Loop through all the columns of the csv (skip first 7 columns)
for column in range(7, len(columns_list)-1):

    #Sort the data frame, biggest numbers first
    sorted_df = df.sort_values(columns_list[column], ascending=False)

    symbol_list = list(sorted_df['Symbol'])
    for i in range(len(symbol_list)):
        symbol_list[i] = symbol_list[i].strip()

    print('column name', columns_list[column])
    for i in range(8):
        print(symbol_list[i])
        if (symbol_list[i] in column_match):
            column_match[symbol_list[i]] += 1
        else:
            column_match[symbol_list[i]] = 1
    print('')


column_match_sorted = sorted(column_match.items(), key=operator.itemgetter(1), reverse=True)
print(column_match_sorted)
