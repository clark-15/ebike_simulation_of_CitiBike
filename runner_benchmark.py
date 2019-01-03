# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:05:40 2018

@author: Dell
"""

# -*- coding: utf-8 -*-
"""
Runner for Sim_random_pick, benchmark
"""
#benchmark first 30 stations: [505, 327, 477, 368, 382, 2006, 465, 435, 426, 358, 514, 284, 285, 168, 151, 3002, 127, 490, 432, 499, 387, 444, 3263, 519, 3255, 492, 379, 359, 293]

#from copy import deepcopy
import Sim_random_pick
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 6)
end_time=start_time+ td(weeks=30)
initial_stations=eval(open(("stations_initial.txt")).read())
estation = [72, 161, 519, 3187, 3203, 3137, 426, 3186, 368, 3254, 3167,3199, 3002, 363, 3267, 423, 251, 3183, 3180, 450]

num_ebike = 0.4
for station in initial_stations.keys():
    initial_stations[station]['ecap']= initial_stations[station]['cap']
    initial_stations[station]['ebike']=round(initial_stations[station]['ecap']*num_ebike)
    initial_stations[station]['bike']=0
    initial_stations[station]['cap']=0
    initial_stations[station]['edock'] = 0

for est in estation:
    initial_stations[est]['edock'] = initial_stations[est]['ecap']
    
    
gc=Sim_random_pick.GlobalClock(start_time,end_time,initial_stations)
gc.clockAdvance()
   

w_demandlost=list(gc.week_demandlost.values())[2:]
w_ebike_return_full=list(gc.week_ebike_return_full.values())[2:]
w_out_of_battery=list(gc.week_out_of_battery.values())[2:]
sum(w_demandlost)/len(w_demandlost)
sum(w_ebike_return_full)/len(w_ebike_return_full)
sum(w_out_of_battery)/len(w_out_of_battery)
