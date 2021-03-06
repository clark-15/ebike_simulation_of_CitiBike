'''
Runner for Sim_random_pick
'''

import Sim_random_pick
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 18)
end_time=start_time+ td(days=1)
initial_stations=eval(open(("stations_initial.txt")).read())
for bikestation in initial_stations.keys():
    initial_stations[bikestation]['ecap']= initial_stations[bikestation]['cap']
    initial_stations[bikestation]['bike']=0
    initial_stations[bikestation]['cap']=0


num_ebike = 0.4

for station in initial_stations.keys():
        initial_stations[station]['ebike']=round(initial_stations[station]['ecap']*num_ebike)
        initial_stations[station]['edock'] = round(initial_stations[station]['ecap']*0.1)



gc=Sim_random_pick.GlobalClock(start_time,end_time,initial_stations)

gc.clockAdvance()
print(gc.demandlost,gc.ebike_return_full,gc.out_of_battery)

with open('stations.csv','w') as f:
    f.write('stationid,tripsin,tripsout,tripsfailedin,tripsfailedout,tripsfailedout_battery,trips_failedout_destinationfull,station_capacity\n')
    for station in gc.stations.keys():
        f.write(str(gc.stations[station].sid)+',')
        f.write(str(gc.stations[station].tripsIn)+',')
        f.write(str(gc.stations[station].tripsOut)+',')
        f.write(str(gc.stations[station].tripsFailedIn)+',')
        f.write(str(gc.stations[station].tripsFailedOut)+',')
        f.write(str(gc.stations[station].tripsFailedOut_Battery)+',')
        f.write(str(gc.stations[station].tripsFailedOut_DestinationFull)+',')
        f.write(str(gc.stations[station].ebike_cap)+'\n')
        
        
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import pandas as pd

stationid=426
outtrips=list(gc.stations[stationid].week_tripsOut.values())[2:]
x = range(1,len(outtrips)+1)
plt.plot(x,outtrips,label = 'tripsOut')
        
outtrips=list(gc.stations[stationid].week_tripsIn.values())[2:]
x = range(1,len(outtrips)+1)
plt.plot(x,outtrips,label = 'tripsIn')     


outtrips=list(gc.stations[stationid].week_tripsFailedOut.values())[2:]
x = range(1,len(outtrips)+1)
plt.plot(x,outtrips,label = 'tripsFailedOut')
   
outtrips=list(gc.stations[stationid].week_tripsFailedIn.values())[2:]
x = range(1,len(outtrips)+1)
plt.plot(x,outtrips,label = 'tripsFailedIn')


outtrips=list(gc.stations[stationid].week_tripsFailedOut_DestinationFull.values())[2:]
x = range(1,len(outtrips)+1)
plt.plot(x,outtrips,label = 'TripsFailedOut_DestinationFull')
plt.legend()
plt.savefig('selectebikes/station426',dpi=300)


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, h

['bike_return_error', 'ebike_return_error', 'lost_demand',
       'three_error', 'out_of_battery', 'average_SOC', 'ebike_trips',
       'all_trips']
    
    



w_demandlost=list(gc.week_demandlost.values())[2:]
w_three_trip_error=list(gc.week_three_trip_error.values())[2:]
w_bike_return_full=list(gc.week_bike_return_full.values())[2:]
w_ebike_return_full=list(gc.week_ebike_return_full.values())[2:]
w_average_SOC=list(gc.week_average_SOC.values())[2:]
w_out_of_battery=list(gc.week_out_of_battery.values())[2:]
w_num_etrip=list(gc.week_num_etrip.values())[2:]
w_num_alltrip=list(gc.week_num_alltrip.values())[2:]
w_demandlost_causedby_battery=list(gc.week_demandlost_causedby_battery)[2:]
x=range(0,len(w_demandlost))    
with open('selectebikes/no_edocks_'+str(num_ebike)+'.csv','w') as f:
     f.write('week,bike_return_error,ebike_return_error,lost_demand,lost_demand_causedby_battery,three_error,ebike_trips,all_trips\n')
     for week in x:
          f.write(str(week+1)+','+str(w_bike_return_full[week])+','+str(w_ebike_return_full[week])+','+str(w_demandlost[week])+','+str(w_demandlost_causedby_battery[week])+','+str(w_three_trip_error[week])+','+str(w_num_etrip[week])+','+str(w_num_alltrip[week])+'\n')




bike_return_error=[]
bike_return_error_st=[]
a= pd.read_csv('selectebikes/no_edocks_0.4.csv')
b=list(a.ebike_return_error+a.lost_demand)
c= list(a.ebike_return_error) 
d=list(a.lost_demand)

plt.plot(range(1,len(b)++1),b)
#plt.plot(range(1,len(b)++1),c)
#plt.plot(range(1,len(b)++1),d)

plt.xlabel('weeks')
plt.ylabel('number of out-of-event')
plt.savefig('selectebikes/benchmark_all_ebike-stations',dpi=300)

sum(outtrips)/20
18500/20
