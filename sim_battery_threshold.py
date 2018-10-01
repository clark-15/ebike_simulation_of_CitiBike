# -*- coding: utf-8 -*-
"""
simulation model with different battery available threshold
"""

import SimData
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 7)
end_time=start_time+ td(weeks=75)
initial_stations=eval(open(("stations_initial.txt")).read())

threshold_list=[0,10,20,30,40,50]

for threshold in threshold_list:
    gc=SimData.GlobalClock(start_time,end_time,initial_stations)
    gc.threshold=threshold
    print('threshold: ',threshold)
    gc.clockAdvance()
    w_demandlost=list(gc.week_demandlost.values())[2:]
    w_three_trip_error=list(gc.week_three_trip_error.values())[2:]
    w_bike_return_full=list(gc.week_bike_return_full.values())[2:]
    w_ebike_return_full=list(gc.week_ebike_return_full.values())[2:]
    w_average_SOC=list(gc.week_average_SOC.values())[2:]
    w_out_of_battery=list(gc.week_out_of_battery.values())[2:]
    w_num_etrip=list(gc.week_num_etrip.values())[2:]
    w_num_alltrip=list(gc.week_num_alltrip.values())[2:]
    x=range(0,len(w_demandlost))    
    with open('simdata/threshold_'+str(threshold)+'.csv','w') as f:
        f.write('week,bike_return_error,ebike_return_error,lost_demand,three_error,out_of_battery,average_SOC,ebike_trips,all_trips\n')
        for week in x:
            f.write(str(week+1)+','+str(w_bike_return_full[week])+','+str(w_ebike_return_full[week])+','+str(w_demandlost[week])+','+str(w_three_trip_error[week])+','+str(w_out_of_battery[week])+','+str(w_average_SOC[week])+','+str(w_num_etrip[week])+','+str(w_num_alltrip[week])+'\n')
                               
            
            
            
            
            
            
            
            
