from random import randint
from collections import OrderedDict
import os
import operator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

MONTE_CARLO_SAMPLE_SIZE = 10000
path = 'Mar13_14/'
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
        print('file_name', file_name)
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

        print('num trades', len(symbols_list))
        equity_graph_list = []
        balance = 0
        position_size = 10000
        for i in range(len(returns_list)):
            percent = returns_list[i]/100
            dollar_change = percent * position_size
            balance += dollar_change
            equity_graph_list.append(balance)
        #print(equity_graph_list)
            
        plt.xlabel('trades')
        plt.ylabel('profit')
        plt.plot(equity_graph_list, label=file_name)
        '''plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)'''
        
        print('all returns', returns_list)

        first_five_trades = round(average_first_num(returns_list, 0, 5),2)
        first_ten_trades = round(average_first_num(returns_list, 0, 10),2)
        five_ten_trades = round(average_first_num(returns_list, 5, 10),2)
        last_five_trades = round(average_first_num(returns_list, len(returns_list)-5, len(returns_list)),2)
        print('average 0-5 trades', first_five_trades)
        print('average 0-10 trades', first_ten_trades)
        print('average 5-10 trades', five_ten_trades)
        print('average last 5 trades', last_five_trades)
        #Print first 5 results and average


        #print('num winners', winners_count)
        #print('num losers', losers_count)
        percent_winners = round(round(float(winners_count)/len(symbols_list),2) * 100)
        print('% winners', percent_winners)

        sum_returns = 0
        for i in range(len(returns_list)):
            sum_returns += returns_list[i]

        actual_return = sum_returns/len(returns_list)
        actual_return = round(actual_return,2)
        print('actual_return per trade', actual_return)
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
        print('')

for file_name in os.listdir(path):
    if file_name.endswith("RESULTS.txt"): 
        calculate_returns(os.path.join(path, file_name))

#Sort by first item in dictionary key, can double index into the tuple, i.e. t[1][3]
results_data_sorted = sorted(results_data.items(), key=lambda t: t[1], reverse=True)

text_file = open(path + "REPORT.txt", "w")
text_file.write('Average index performance: ' + '\n\n')
text_file.write('FORMAT: scan_name, 0-5 trades, 0-10 trades, 5-10 trades, last 5 trades, ' + 
                'average_trade_return, accuracy, variance,' + '\n\n')

for scan in results_data_sorted:
    text_file.write(str(scan) + '\n')

text_file.close()

plt.savefig(path + 'Results.png')
