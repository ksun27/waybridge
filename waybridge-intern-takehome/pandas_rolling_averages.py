# Solving for Rolling Averages using Pandas - Kevin Sun

#Libraries Needed:
#- Pandas
#- Matplotlib
#- datetime

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

data = pd.read_csv('example.csv')
del data['index']
data['time'] = pd.to_datetime(data['time'], unit='s') 
data = data.set_index('time')

data['average'] = data.rolling('600s').mean()
data['average'].loc[data.index < pd.Timestamp(1970, 1, 1, 0, 10)] = None
data.index = (data.index - dt.datetime(1970,1,1)).total_seconds()

values = (data['average'].max(), max(data.index.tolist()), data['value'].max())

colors = ['lightblue','darkorange']
data.plot(color=colors, linewidth=3, figsize=(12,6))

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend('')

plt.title('Rolling Average with Window of 600s', fontsize=20)
plt.xlabel('Time', fontsize=16)
plt.ylabel('Average', fontsize=16)

#To view an annotated version of this code, please refer to the jupyter notebook of the same name
