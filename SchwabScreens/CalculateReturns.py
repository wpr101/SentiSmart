from random import randint
from collections import OrderedDict
import os
import operator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

MONTE_CARLO_SAMPLE_SIZE = 10000
TOP_NUM_COLUMNS = 15

path = 'March/Mar28_29/'
scan_report_folder = 'Scan_Report/'
results_data = {}

def percent_change(startPoint, currentPoint):
    return ((float(currentPoint) - startPoint)/abs(startPoint))*100.00

#calculate the average return for a specific range of trades
def average_first_num(returns_list, start, end):
    average_first_five = 0
    for i in range(start,end):
        average_first_five += returns_list[i]
    average_first_five = average_first_five/(end-start)
    return(average_first_five)

def calculate_returns(file_name):
    with open(file_name, "r") as f:
        symbols_list = []
        returns_list = []
        winners_count = 0
        losers_count = 0
        for line in f:
            symbol, start_price, sell_price = line.split()
            start_price = float(start_price)
            sell_price = float(sell_price)
            change = round(percent_change(start_price, sell_price),2)
            if (change > 0):
                winners_count += 1
            elif (change < 0):
                losers_count += 1
            symbols_list.append(symbol)
            returns_list.append(change)

        equity_graph_list = []
        balance = 0
        position_size = 10000
        for i in range(len(returns_list)):
            percent = returns_list[i]/100
            dollar_change = percent * position_size
            balance += dollar_change
            equity_graph_list.append(balance)
            
        plt.xlabel('trades')
        plt.ylabel('profit')
        plt.plot(equity_graph_list, label=file_name)
        '''plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)'''

        first_five_trades = round(average_first_num(returns_list, 0, 5),2)
        first_ten_trades = round(average_first_num(returns_list, 0, 10),2)
        five_ten_trades = round(average_first_num(returns_list, 5, 10),2)
        last_five_trades = round(average_first_num(returns_list, len(returns_list)-5, len(returns_list)),2)

        percent_winners = round(round(float(winners_count)/len(symbols_list),2) * 100)

        sum_returns = 0
        for i in range(len(returns_list)):
            sum_returns += returns_list[i]

        actual_return = sum_returns/len(returns_list)
        actual_return = round(actual_return,2)

        variance = round(np.var(returns_list),2)

        #create dictionary entry for data to write to file
        results_data[file_name] = (first_five_trades, first_ten_trades, five_ten_trades, last_five_trades,
                                    actual_return, percent_winners, variance )

        '''
        max_return = 0
        min_return = 0
        for a in range(0,MONTE_CARLO_SAMPLE_SIZE):
            average_monte_carlo_return = 0
            monte_carlo_return = 0
            for i in range(len(returns_list)):
                index = randint(0,len(returns_list)-1)
                monte_carlo_return += returns_list[index]
            average_monte_carlo_return = monte_carlo_return/len(returns_list)
            #print('monte_carlo_return', round(average_monte_carlo_return,2))

            if (average_monte_carlo_return > max_return):
                max_return = average_monte_carlo_return

            if (average_monte_carlo_return < min_return):
                min_return = average_monte_carlo_return'''

        #print('max_random_return', round(max_return,2))
        #print('min_random_return', round(min_return,2))

        '''averaged_random_return = 0
        for i in range(MONTE_CARLO_SAMPLE_SIZE):
            index = randint(0,len(returns_list)-1)
            averaged_random_return += returns_list[index]
        averaged_random_return = averaged_random_return/MONTE_CARLO_SAMPLE_SIZE
        print('averaged_random_returns',round(averaged_random_return,2))'''

        '''random_runs = []
        for i in range(10):
            random_sample = 0
            for i in range(len(returns_list)):
                index = randint(0,len(returns_list)-1)
                random_sample += returns_list[index]
            random_sample = random_sample/len(returns_list)
            random_runs.append(round(random_sample,2))
        print("random runs", random_runs)'''


d=path
#Complicated statement to get all the directories except the TRADING directory
dir_list = [os.path.join(d,o) for o in os.listdir(d) if (os.path.isdir(os.path.join(d,o)) and (not ('TRADING' in os.path.join(d,o))))]
for i in range(len(dir_list)):
    dir_list[i] += '/'

summary_list = []
column_performance = {}
column_bad_performance = {}
#Loop through all the folders in the directory containing txt results
for directory in dir_list:
    print('directory', directory)
    for file_name in os.listdir(directory):
        if file_name.endswith("RESULTS.txt"): 
            calculate_returns(os.path.join(directory, file_name))

    #Sort by first item in dictionary key, can double index into the tuple, i.e. t[1][3]
    results_data_sorted = sorted(results_data.items(), key=lambda t: t[1], reverse=True)

    #loop through the top performing 15 columns
    for i in range(TOP_NUM_COLUMNS):
        #remove the path to find column name
        removed_path = results_data_sorted[i][0].split('/')[-1]
        #remove the .txt extension to the file name only
        column_name_only = removed_path.split('_')[0]
        if (column_name_only in column_performance):
            column_performance[column_name_only] += 1
        else:
            column_performance[column_name_only] = 1

    #loop through the worst performing 15 columns
    for i in range(len(results_data_sorted) - TOP_NUM_COLUMNS, len(results_data_sorted)-1):
        #remove the path to find column name
        removed_path = results_data_sorted[i][0].split('/')[-1]
        #remove the .txt extension to the file name only
        column_name_only = removed_path.split('_')[0]

        if (column_name_only in column_bad_performance):
            column_bad_performance[column_name_only] += 1
        else:
            column_bad_performance[column_name_only] = 1

    #make new directory for reporting about the scan
    reports_directory = directory + scan_report_folder
    if not os.path.exists(reports_directory):
        os.makedirs(reports_directory)

    text_file = open(reports_directory + "REPORT.txt", "w")
    text_file.write('Average index performance: ' + '\n\n')
    text_file.write('FORMAT: scan_name, 0-5 trades, 0-10 trades, 5-10 trades, last 5 trades, ' + 
                    'average_trade_return, accuracy, variance,' + '\n\n')

    for scan in results_data_sorted:
        text_file.write(str(scan) + '\n')

    summary_list.append(results_data_sorted[0])

    text_file.close()

    plt.savefig(reports_directory + 'Results.png')
    plt.clf()
    #reset the data for next directory
    results_data = {}


#Make a final summary report
summary_file = open(path + "SUMMARY.txt", "w")
summary_file.write('DOW daily performance: ' + '\n')
summary_file.write('Nasdaq daily performance: ' + '\n\n')
summary_file.write('FORMAT: scan_name, 0-5 trades, 0-10 trades, 5-10 trades, last 5 trades, ' + 
                    'average_trade_return, accuracy, variance,' + '\n\n')
summary_file.write('***Results are sorted by average_trade_return***' + '\n\n')

#sort by average_trade_return which is t[1][4]
summary_list_sorted = sorted(summary_list, key=lambda t: t[1][4], reverse=True)


for i in range(len(summary_list_sorted)):
    summary_file.write(str(summary_list_sorted[i]) + '\n\n')

summary_file.write('Top (' + str(TOP_NUM_COLUMNS) + ') performing columns across daily scans' + '\n')
#Examine top performing columns
sorted_column_performance = sorted(column_performance.items(), key=operator.itemgetter(1), reverse=True)
for item in sorted_column_performance:
    #check which performance metrics show up more than once in top accross the scans
    if (item[1] > 2):
        summary_file.write(str(item) + '\n')

summary_file.write('\n')
summary_file.write('Worst (' + str(TOP_NUM_COLUMNS) + ') performing columns across daily scans' + '\n')
bad_column_performance = sorted(column_bad_performance.items(), key=operator.itemgetter(1), reverse=True)
for item in bad_column_performance:
    #check which performance metrics show up more than once in top accross the scans
    if (item[1] > 2):
        summary_file.write(str(item) + '\n')


summary_file.close()



