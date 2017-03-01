from random import randint

def percent_change(startPoint, currentPoint):
    return ((float(currentPoint) - startPoint)/abs(startPoint))*100.00

MONTE_CARLO_SAMPLE_SIZE = 10000


with open("Feb27_28/Results_Strat1.txt", "r") as f:
    symbols_list = []
    returns_list = []
    for line in f:
        symbol, start_price, sell_price = line.split()
        start_price = float(start_price)
        sell_price = float(sell_price)
        change = round(percent_change(start_price, sell_price),2)
        symbols_list.append(symbol)
        returns_list.append(change)

    #print(symbols_list)
    #print(returns_list)
    '''returns_list = [5, percent_change(17.18,16.49), percent_change(830.68,808.57),
                    percent_change(69.24,75.59), percent_change(40.72,38.53),
                    percent_change(26.17,25.10), percent_change(63.52,55.12),
                    percent_change(89.77,88.49), percent_change(84.84,88.00),
                    percent_change(120.52,115.33), percent_change(21.81,22.79)]'''

    sum_returns = 0
    for i in range(len(returns_list)):
        sum_returns += returns_list[i]
        #print('sum',sum_returns)
        #print('current',returns_list[i])
        #print('')
    actual_return = sum_returns/len(returns_list)   
    print('actual_return', round(actual_return,2))

    
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
            min_return = average_monte_carlo_return

    print('max_random_return', round(max_return,2))
    print('min_random_return', round(min_return,2))

    averaged_random_return = 0
    for i in range(MONTE_CARLO_SAMPLE_SIZE):
        index = randint(0,len(returns_list)-1)
        averaged_random_return += returns_list[index]
    averaged_random_return = averaged_random_return/MONTE_CARLO_SAMPLE_SIZE
    print('averaged_random_returns',round(averaged_random_return,2))

    random_runs = []
    for i in range(10):
        random_sample = 0
        for i in range(len(returns_list)):
            index = randint(0,len(returns_list)-1)
            random_sample += returns_list[index]
        random_sample = random_sample/len(returns_list)
        random_runs.append(round(random_sample,2))
    print("random runs", random_runs)

