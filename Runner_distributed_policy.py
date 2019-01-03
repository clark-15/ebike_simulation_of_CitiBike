# -*- coding: utf-8 -*-
"""
Runner for distributed policy
"""


import Sim_random_pick
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 18)
end_time=start_time+ td(weeks=50)
initial_stations=eval(open(("stations_initial.txt")).read())

import csv
station_rank = []
station_demand_percentage = {}
with open('data/20weeks_ranked.csv') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        station_rank.append(int(row[0]))
        station_demand_percentage[int(row[0])] = float(row[9])


for bikestation in initial_stations.keys():
    initial_stations[bikestation]['ecap']= initial_stations[bikestation]['cap']
    initial_stations[bikestation]['bike']=0
    initial_stations[bikestation]['cap']=0
    


total_edock_ratio_list = [0.1,0.2,0.25,0.3,0.4]
num_ebike = 0.4


for total_edock_ratio in total_edock_ratio_list:
    print('ratio:',total_edock_ratio)
    total_dock_number = 0
    for station in initial_stations.keys():
        total_dock_number += initial_stations[station]['ecap']
        
    total_edock_number =  total_edock_ratio * total_dock_number
    edock_num = 0
    for station in initial_stations.keys():
            initial_stations[station]['ebike']=round(initial_stations[station]['ecap']*num_ebike)
            initial_stations[station]['edock'] = round(station_demand_percentage[station]*total_edock_number)
    
    
               
    gc=Sim_random_pick.GlobalClock(start_time,end_time,initial_stations)
    gc.clockAdvance()
    
    w_demandlost=list(gc.week_demandlost.values())[2:]
    #w_bike_return_full=list(gc.week_bike_return_full.values())[2:]
    w_ebike_return_full=list(gc.week_ebike_return_full.values())[2:]
    w_average_SOC=list(gc.week_average_SOC.values())[2:]
    w_out_of_battery=list(gc.week_out_of_battery.values())[2:]
    w_num_etrip=list(gc.week_num_etrip.values())[2:]
    #w_num_alltrip=list(gc.week_num_alltrip.values())[2:]
    x=range(0,len(w_demandlost))    
    with open('simdata/distributed_policy_total_edock_ratio_'+str(total_edock_ratio)+'.csv','w') as f:
        f.write('week,ebike_return_error,lost_demand,out_of_battery_trips,ebike_trips\n')
        for week in x:
            f.write(str(week+1)+','+str(w_ebike_return_full[week])+','+str(w_demandlost[week])+','+str(w_out_of_battery[week])+','+str(w_num_etrip[week])+'\n')
                               
        




        