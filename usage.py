'''
usage for each station based on Sim_random_pick.py
'''

import Sim_random_pick
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 18)
end_time=start_time+ td(weeks=20)
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
        
        