'''
Runner for average_soc_output.py
'''

import average_soc_output
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 18)
end_time=start_time+ td(days=2)
initial_stations=eval(open(("stations_initial.txt")).read())
for bikestation in initial_stations.keys():
    initial_stations[bikestation]['ecap']= initial_stations[bikestation]['cap']
    initial_stations[bikestation]['bike']=0
    initial_stations[bikestation]['cap']=0


num_ebike = 0.4

for station in initial_stations.keys():
        initial_stations[station]['ebike']=round(initial_stations[station]['ecap']*num_ebike)
        initial_stations[station]['edock'] = round(initial_stations[station]['ecap']*0)



gc=average_soc_output.GlobalClock(start_time,end_time,initial_stations)

gc.clockAdvance()
gc.week_demandlost
(gc.t -gc.start_time).days


import matplotlib.pyplot as plt
a= list(gc.week_average_SOC.values())
b= list(gc.week_average_SOC.keys())
c= list(map(lambda x:x/6,b))
plt.plot(c,a)
plt.scatter(c,a,s = 1)
plt.ylabel('average SOC')
plt.xlabel('hours')
plt.title('Start at 18:00, average SOC vs hours')
plt.savefig('SOC_vs_hours',dpi = 300)

