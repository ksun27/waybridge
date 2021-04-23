# Waybridge Technical Assessment - Kevin Sun

This repository contains Kevin Sun's Waybridge Technical Assessment. 

It is split into two parts: 
1. Calculating the Rolling Average using Pandas
2. Calculating the Rolling Average using Python (Algorithmic)

Both parts have a jupyter notebook file and a python file. For better viewing experience, I recommend viewing the jupyter notebook files as they are annotated with my comments and show output.

Some comments about the assessment:

- The rolling averages differ by a slight amount. I am unsure on what is causing this difference, however I believe the difference is negligible. 
- For calculate_rolling_average (returns tuple: Max value of avgs, times, values), I was confused on what was meant by times and values, so I simply added the max time and max value into the tuple.
- For both solutions, I did a window of 600 seconds
- For Pandas: To solve for a given rolling average at a certain point, simply just index into the column at the time and find the average.
- For Python: To solve for a given rolling average at a certain point, we can modify the array to store a tuple of time and average to get the average that corresponds to correct element of time_array.

Thank you for the opportunity to take this challenge!

