'''
Runner for Sim_random_pick_out-of-battery-trip-selection.py
'''

import Sim_random_pick_out_of_battery_trip_dest_selection
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 6)
end_time=start_time+ td(days=1)
initial_stations=eval(open(("stations_initial.txt")).read())
num_ebike = 0.4
for station in initial_stations.keys():
    initial_stations[station]['ecap']= initial_stations[station]['cap']
    initial_stations[station]['ebike'] = round(initial_stations[station]['ecap']*num_ebike)
    initial_stations[station]['edock'] = 0
    initial_stations[station]['bike']=0
    initial_stations[station]['cap']=0



gc=Sim_random_pick_out_of_battery_trip_dest_selection.GlobalClock(start_time,end_time,initial_stations)
gc.clockAdvance()

dest_count = {}
for sta in gc.stations.keys():
    dest_count[sta] = gc.stations[sta].dest_out_of_battery

sorted_dest_count_list = sorted(dest_count.items(), key=lambda kv: kv[1],reverse = True)
with open('dest_out_of_battery_iteration.csv','w') as f:
    f.write('station,out-of-battery-as-a-dest\n')
    for i in sorted_dest_count_list:
        f.write(str(i[0])+','+str(i[1])+'\n')

steady = {}
for i in gc.stations.keys(): 
    temp={}   
    temp['ebike'] = gc.stations[i].ebike
    temp['ecap'] = gc.stations[i].ebike_cap
    temp['edock'] = gc.stations[i].edock
    temp['bike'] = 0
    temp['cap'] = 0
    steady[i] = temp

f = open("stations_initial.txt","w")
f.write( str(steady) )
f.close()