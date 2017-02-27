def gains_per_trade(per_trade_gain, equity):
    
    percent_needed = per_trade_gain/equity
    return percent_needed * 100


per_trade_gain = 200.00
equity = 100000.00

print(gains_per_trade(per_trade_gain, equity))
