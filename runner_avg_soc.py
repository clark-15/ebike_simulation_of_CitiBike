# -*- coding: utf-8 -*-
"""
Runner for average soc
"""

import Sim_random_pick
from datetime import timedelta as td
from datetime import datetime as time
from copy import deepcopy
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

N = 200
initial_stations_copy = deepcopy(initial_stations)

gc=Sim_random_pick.GlobalClock(start_time,end_time,dict(initial_stations))
gc.clockAdvance()
a=[]


for i in range(N):
    gc=Sim_random_pick.GlobalClock(start_time,end_time,dict(initial_stations))
    gc.clockAdvance()
    minSOC, minst = 101, -1
    st_avg = {}
    for key,st in gc.stations.items():
        sum = 0
        if len(st.ebike) == 0: continue
        for bike in st.ebike.values():
            sum += bike.SOC
        avg = sum / len(st.ebike)
        st_avg[key] = avg
        if avg<minSOC:
            minSOC = avg
            minst = key
    print(minst,minSOC,i)
    #initial_stations[minst]['edock'] = initial_stations[minst]['ecap']    
    initial_stations_copy[minst]['edock'] = initial_stations_copy[minst]['ecap']
    initial_stations = initial_stations_copy

for k in gc.
