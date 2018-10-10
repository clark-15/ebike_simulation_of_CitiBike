# -*- coding: utf-8 -*-
"""
analysis the result of proportion_of_bike.py
"""

#import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats




a= pd.read_csv('simdata/propotion_of_bike_all_bike0.1.csv')

a.columns
plt.plot(a.week,a.bike_return_error)
plt.plot(a.week,a.ebike_return_error)
plt.plot(a.week,a.lost_demand)
plt.plot(a.week,a.three_error)
plt.plot(a.week,a.out_of_battery)
plt.plot(a.week,a.average_SOC)
plt.plot(a.week,a.ebike_trips)
plt.plot(a.week,a.all_trips)

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, h


error=[]
['bike_return_error', 'ebike_return_error', 'lost_demand',
       'three_error', 'out_of_battery', 'average_SOC', 'ebike_trips',
       'all_trips']
    
    
    
propotion_of_bike_list=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] 
bike_return_error=[]
bike_return_error_st=[]
for proportion in  propotion_of_bike_list:
    s='simdata/propotion_of_bike_all_bike'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list(a.bike_return_error+a.lost_demand)[25:]
    average_five_week  = []
    for i in range(10):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(propotion_of_bike_list,bike_return_error,yerr=bike_return_error_st,ecolor='red',capsize=3)    
plt.xlabel('initial ratio of bikes to docks')
plt.ylabel('number of out-of-event error')
plt.title('number of out-of-event VS number of bikes\n all demands are bikes')
plt.savefig('simdata/number of out-of-event VS number of bikes_all_bike',dpi = 300,bbox_inches='tight')


propotion_of_bike_list=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] 
bike_return_error=[]
bike_return_error_st=[]
for proportion in  propotion_of_bike_list:
    s='simdata/propotion_of_bike_'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list(a.bike_return_error/(a.all_trips-a.ebike_trips))[15:]
    average_five_week  = []
    for i in range(12):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(propotion_of_bike_list,bike_return_error,yerr=bike_return_error_st,ecolor='red',capsize=3)    
plt.xlabel('initial ratio of bikes to docks')
plt.ylabel('ratio of bike_return_error to number of bike trips')
plt.title('ratio of bike_return_error to number of bike trips\n VS number of bikes')

plt.savefig('ratio of bike_return_error to number of bike trip',dpi = 300,bbox_inches='tight')

 

  

propotion_of_bike_list=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] 
bike_return_error=[]
bike_return_error_st=[]
for proportion in  propotion_of_bike_list:
    s='simdata/propotion_of_bike_'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list(a.bike_return_error+a.ebike_return_error+a.lost_demand+a.out_of_battery)[15:]
    average_five_week  = []
    for i in range(12):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(propotion_of_bike_list,bike_return_error,yerr=bike_return_error_st,ecolor='red',capsize=3)    
plt.xlabel('initial ratio of bikes to docks')
plt.ylabel('number of out-of-events in one week')
plt.title('number of out-of-events (return error, lost demand, out-of-battery) \n VS number of bikes')

plt.savefig('number of out-of-event VS number of bikes',dpi = 300,bbox_inches='tight')





# width of the bars
barWidth = 0.3

# Choose the height of the blue bars
bars1 = [10, 9, 2]

# Choose the height of the cyan bars
bars2 = [10.8, 9.5, 4.5]

# Choose the height of the error bars (bars1)
yer1 = [2, 0.4, 0.5]

# Choose the height of the error bars (bars2)
yer2 = [1, 0.7, 1]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

# Create blue bars


# Create cyan bars
plt.errorbar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='sorgho')

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['cond_A', 'cond_B', 'cond_C'])
plt.ylabel('height')
plt.legend()