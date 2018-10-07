# -*- coding: utf-8 -*-

#import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats




a= pd.read_csv('simdata/propotion_of_bike_0.1.csv')

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



for column in ['bike_return_error', 'ebike_return_error', 'lost_demand',
       'three_error', 'out_of_battery', 'average_SOC', 'ebike_trips',
       'all_trips']:
    
    
    
threshold_list=[0,5,10,15,20,25,30] 
bike_return_error=[]
bike_return_error_st=[]
for threshold in  threshold_list:
    s='simdata_threshold/simdata/threshold_'+str(threshold)+'.csv'
    a= pd.read_csv(s)
    b=list(a.three_error)[2:]
    average_five_week  = []
    for i in range(10):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(threshold_list,bike_return_error,yerr=bike_return_error_st,ecolor='red',capsize=3)    
plt.xlabel('SOC threshold')
plt.ylabel('number of three-trip error')
plt.title('three-trip-error VS SOC threshold\n 10 batches, each batch lasts 5 weeks')

plt.savefig('simdata_threshold/bike return error VS three-trip-error',dpi = 300,bbox_inches='tight')






threshold_list=[0,5,10,15,20,25,30] 
bike_return_error=[]
bike_return_error_st=[]
for threshold in  threshold_list:
    s='simdata_threshold/simdata/threshold_'+str(threshold)+'.csv'
    a= pd.read_csv(s)
    b=list(a.ebike_return_error/(a.ebike_trips))[2:]
    average_five_week  = []
    for i in range(10):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(threshold_list,bike_return_error,yerr=bike_return_error_st,ecolor='red',capsize=3)    
plt.xlabel('SOC threshold')
plt.ylabel('ratio of ebike_return_error to number of bike trips')
plt.title('ratio of ebike_return_error to number of bike trips VS SOC threshold')

plt.savefig('simdata_threshold/ratio of ebike_return_error to number of bike trips VS SOC threshold',dpi = 300,bbox_inches='tight')







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

plt.savefig('simdata_threshold/ratio of bike_return_error to number of bike trip',dpi = 300,bbox_inches='tight')

 

  

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

plt.savefig('simdata_threshold/number of out-of-event VS number of bikes',dpi = 300,bbox_inches='tight')





