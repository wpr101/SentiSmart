def percent_change(startPoint, currentPoint):
    return ((float(currentPoint) - startPoint)/abs(startPoint))*100.00


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

    sum_returns = 0
    for i in range(len(returns_list)):
        sum_returns += returns_list[i]
        #print('sum',sum_returns)
        #print('current',returns_list[i])
        #print('')
    average_return = sum_returns/len(returns_list)   
    print(average_return)

