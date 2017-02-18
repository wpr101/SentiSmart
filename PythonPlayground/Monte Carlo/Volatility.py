import math

def variance(data):
    avg_data = mean(data)
    sum_of_squares = 0.00
    for i in range(len(data)):
        diff = data[i] - avg_data
        diff_squared = diff * diff
        sum_of_squares += diff_squared

    #for some strange reason wiki says to divide by n-1
    sum_of_squares = sum_of_squares/(len(data) - 1)
    return(sum_of_squares)

def volatility():
    sd = .01
    year = 1.00/252.00 #252 trading days in a year

    yearly_volatility = sd / math.sqrt(year)
    monthly_volatility = yearly_volatility * math.sqrt(1.00/12.00)

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

#average distance to the mean
def std_dev(data):
    average = 0.00
    for i in range(len(data)):
        average += data[i]

    average = average/len(data)
    sum_of_squares = 0
    for i in range(len(data)):
        diff = average - data[i]
        diff_squared = diff * diff
        sum_of_squares += diff_squared

    sum_of_squares = sum_of_squares/(len(data)-1)


    return(math.sqrt(sum_of_squares))

Q4_2016_results = [5.47, 1.87, 0.41, -2.09, -5.01, -0.73, 
                   -3.54, 9.17, -4.08, -13.22, -1.43, 3.72,
                   -4.31, 4.49]

variance_sample = [17.00, 15.00, 23.00, 7.00, 9.00, 13.00]


print('mean', mean(Q4_2016_results))
print('std_dev', std_dev(variance_sample))
print('variance', variance(variance_sample))

#print('variance', variance(variance_sample))

