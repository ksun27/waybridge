# Solving for Rolling Averages using Python - Kevin Sun

#Libraries Needed:
#- csv

import csv

''' example.csv contains the values for the system.

    Example call
    ===========
    time_array, input_array = load_csv()
    max_value, rolling_times, rolling_avgs = calculate_rolling_average(time_array, input_array, averaging_period=600)

'''

def load_csv():
    """ load the CSV containing the values.

    Returns:
        tuple: first element sampling points, second element values

    """
    time_array = []
    input_array = []
    with open('example.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            if index > 0:
                time_array.append(int(float(row[1])))
                input_array.append(int(float(row[2])))

    return time_array, input_array


def calculate_rolling_average(time_array, input_array, averaging_period=600):
    """Summary
    Calculate a rolling average. The output of this function could be second by second, or just the same sampled time points as the input, depending on how you want to implement your algorithm.

    Args:
        time_array (list): sampling points
        input_array (list): values
        averaging_period (int): (optional) default 10 minutes (600s)

    Returns:
        tuple: Max value of avgs, times, values
    """
    rolling_averages = []
    i = 0
    j = 0
    total = 0
    while j < len(time_array):
        while time_array[j] - time_array[i] <= averaging_period:
            j += 1
            if j >= len(time_array) or i >= len(time_array):
                break
        for k in range(i, j-1):
            total += input_array[k]
        average = total/(j-1-i)
        rolling_averages.append(average)
        total = 0
        i += 1
    return (max(rolling_averages), time_array, input_array)

time_array, input_array = load_csv()
result = calculate_rolling_average(time_array, input_array, 600)
print(result)

#To view an annotated version of this code, please refer to the jupyter notebook of the same name
