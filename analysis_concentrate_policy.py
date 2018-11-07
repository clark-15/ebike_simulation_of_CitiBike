
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats


#['week', 'ebike_return_error', 'lost_demand', 'out_of_battery_trips','ebike_trips']

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, h

total_edock_ratio_list = [0,0.05,0.1,0.2,0.3,0.4,0.5,1]




bike_return_error=[]
bike_return_error_st=[]
for proportion in  total_edock_ratio_list:
    s='simdata/concentrated_policy_total_edock_ratio_'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list(a.ebike_return_error)[15:]
    average_five_week  = []
    for i in range(7):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(total_edock_ratio_list,bike_return_error,yerr=bike_return_error_st,c= 'b',ecolor='red',capsize=3\
             ,label = 'return error')    
plt.xlabel('edocks / total docks')
plt.ylabel('number of return errors in one week')
plt.title('concentrated policy ranked by total demand\n 90 percent edocks in each selected station')
#plt.savefig('simdata/policy_result/concentrate_return',dpi = 300,bbox_inches='tight')

bike_return_error=[]
bike_return_error_st=[]
for proportion in  total_edock_ratio_list:
    s='simdata/concentrated_policy_total_edock_ratio_'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list(a.lost_demand)[15:]
    average_five_week  = []
    for i in range(7):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(total_edock_ratio_list,bike_return_error,yerr=bike_return_error_st,c= 'y',ecolor='red',capsize=3\
             ,label = 'demand loss')    
plt.xlabel('edocks / total docks')
plt.ylabel('number of demand loss in one week')
plt.title('concentrated policy ranked by total demand\n 90 percent edocks in each selected station')
#plt.savefig('simdata/policy_result/concentrate_demand',dpi = 300,bbox_inches='tight')


bike_return_error=[]
bike_return_error_st=[]
for proportion in  total_edock_ratio_list:
    s='simdata/concentrated_policy_total_edock_ratio_'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list(a.out_of_battery_trips)[15:]
    average_five_week  = []
    for i in range(7):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(total_edock_ratio_list,bike_return_error,yerr=bike_return_error_st,c = 'g',ecolor='red',capsize=3\
             ,label = 'out-of-battery trips')    
plt.xlabel('edocks / total docks')
plt.ylabel('out-of-battery trips in one week')
plt.title('concentrated policy ranked by total demand\n 90 percent edocks in each selected station')
#plt.savefig('simdata/policy_result/concentrate_battery',dpi = 300,bbox_inches='tight')
plt.legend()
plt.savefig('simdata/policy_result/concentrate_all',dpi = 300,bbox_inches='tight')


bike_return_error=[]
bike_return_error_st=[]
for proportion in  total_edock_ratio_list:
    s='simdata/concentrated_policy_total_edock_ratio_'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list(a.out_of_battery_trips+a.lost_demand+a.ebike_return_error)[15:]
    average_five_week  = []
    for i in range(7):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(total_edock_ratio_list,bike_return_error,yerr=bike_return_error_st,c= 'b',ecolor='red',capsize=3\
             ,label = 'concentrated')    
plt.xlabel('edocks / total docks')
plt.ylabel('Total out-of-event in one week')
plt.title('Total out-of-event trips\n 90 percent edocks in each selected station')
plt.legend()

bike_return_error=[]
bike_return_error_st=[]
for proportion in  total_edock_ratio_list:
    s='simdata/simdata/distributed_policy_total_edock_ratio_'+str(proportion)+'.csv'
    a= pd.read_csv(s)
    b=list(a.out_of_battery_trips+a.lost_demand+a.ebike_return_error)[15:]
    average_five_week  = []
    for i in range(7):
        average_five_week.append(sum(b[(5*i):(5*i+5)])/5)
    mean, error=mean_confidence_interval(average_five_week)
    bike_return_error.append(mean)
    bike_return_error_st.append(error)
plt.errorbar(total_edock_ratio_list,bike_return_error,yerr=bike_return_error_st,c= 'g',ecolor='red',capsize=3\
             ,label = 'distributed')    
plt.xlabel('edocks / total docks')
plt.ylabel('Total out-of-event in one week')
plt.title('Total out-of-event trips ')
plt.legend()
plt.savefig('simdata/policy_result/comparison',dpi = 300,bbox_inches='tight')

s='simdata/simdata/distributed_policy_total_edock_ratio_0.csv'
a= pd.read_csv(s)
b=list(a.ebike_trips - a.out_of_battery_trips)[2:]
c= list(a.week)[2:]
plt.plot(c,b)
s='simdata/concentrated_policy_total_edock_ratio_0.csv'
a= pd.read_csv(s)
b=list(a.ebike_trips - a.out_of_battery_trips)[2:]
c= list(a.week)[2:]
plt.plot(c,b)

