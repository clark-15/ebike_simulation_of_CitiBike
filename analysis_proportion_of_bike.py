# -*- coding: utf-8 -*-
"""
analysis the result of proportion_of_bike.py
"""

#import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats




a= pd.read_csv('simdata/propotion_of_bike_all_bike0.4.csv')
b=list((a.lost_demand_causedby_battery/a.lost_demand))
plt.scatter(a.week,b)
plt.ylim(0,0.001)
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
    
    
    
propotion_of_bike_list=[0.3,0.4,0.5,0.6,0.7] 
bike_return_error=[]
bike_return_error_st=[]
for proportion in  propotion_of_bike_list:
    s='simdata/propotion_of_bike_all_bike'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list((a.lost_demand))[15:]
    average_five_week  = []
    for i in range(7):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(propotion_of_bike_list,bike_return_error,yerr=bike_return_error_st,ecolor='red',capsize=3,label = 'bike')    
plt.xlabel('initial ratio of bikes to docks')
plt.ylabel('demand loss rate (bike)')
plt.title('demand loss rate (bike)')

###delte later

propotion_of_bike_list=[0.3,0.4,0.5,0.6,0.7] 
bike_return_error=[]
bike_return_error_st=[]
for proportion in  propotion_of_bike_list:
    s='simdata_ebike_allebike/simdata_ebike/propotion_of_ebike_'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list((a.ebike_return_error))[15:]
    average_five_week  = []
    for i in range(7):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(propotion_of_bike_list,bike_return_error,yerr=bike_return_error_st,c='orange',ecolor='red',capsize=3,label = 'ebike')    
plt.xlabel('initial ratio of (e)bikes to (e)docks')
ty='return error'
plt.ylabel('number of '+ty)
plt.legend()
plt.title('number of '+ty+' VS number of ebikes ')


plt.savefig('number of '+ty+' VS number of ebikes before increasing arrival rate',dpi = 300,bbox_inches='tight')



propotion_of_bike_list=[0.3,0.4,0.5,0.6,0.7] 
bike_return_error=[]
bike_return_error_st=[]
for proportion in  propotion_of_bike_list:
    s='simdata/propotion_of_bike_all_bike'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list((a.lost_demand+a.bike_return_error))[25:]
    average_five_week  = []
    for i in range(10):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(propotion_of_bike_list,bike_return_error,yerr=bike_return_error_st,c= 'orange',ecolor='red',capsize=3) 
plt.xlabel('initial ratio of bikes to docks')
plt.ylabel('demand loss rate (bike)')
plt.title('demand loss rate (bike)')

   


 
propotion_of_bike_list=[0.3,0.4,0.5,0.6,0.7] 
bike_return_error=[]
bike_return_error_st=[]
for proportion in  propotion_of_bike_list:
    s='simdata_ebike(1)_higher_rate/simdata_ebike/propotion_of_ebike_'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list(a.ebike_return_error+a.lost_demand+a.out_of_battery)[15:]
    average_five_week  = []
    for i in range(7):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(propotion_of_bike_list,bike_return_error,yerr=bike_return_error_st,ecolor='red', c='orange',capsize=3)    
plt.xlabel('initial ratio of ebikes to edocks')
plt.ylabel('number of out-of-event')
plt.title('number of out-of-events VS number of ebikes\n all demands are ebikes')



plt.savefig('simdata/demand loss rate (bike)',dpi = 300,bbox_inches='tight')


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


