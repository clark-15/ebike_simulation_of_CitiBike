'''
\u613f\u672a\u6765\u6211\u4eec\u8fd8\u6709\u4ea4\u96c6\uff0c\u90a3\u65f6\u6211\u4e00\u5b9a\u4e0d\u4f1a\u653e\u5f03

the runner of simulation of ebikes

'''



import SimData
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 7)
end_time=start_time+ td(weeks=20)
initial_stations=eval(open(("stations_initial.txt")).read())


gc=SimData.GlobalClock(start_time,end_time,initial_stations)

gc.clockAdvance()

import pickle
gc=pickle.load(open('gc_20weeks.pickle','rb'))

len(gc.demandlost)
sum(gc.week_demandlost.values())




gc.week_demandlost
gc.week_three_trip_error
gc.week_bike_return_full
gc.week_ebike_return_full

import matplotlib.pyplot as plt

di=gc.week_demandlost
di=gc.week_three_trip_error
di=gc.week_bike_return_full
di = gc.week_ebike_return_full

a=list(di.values())
b=list(di.keys())
plt.scatter(b,a)
plt.plot(b,a)
plt.xlabel('week')
s='demand lost in a week'
plt.ylabel(s)
plt.savefig(s,dpi=300)


percent=[]
epercent=[]
for i in gc.stations.keys():
    if gc.stations[i].ebike_cap != 0 and gc.stations[i].bike_cap != 0:
        percent.append(len(gc.stations[i].bike)/gc.stations[i].bike_cap)
        epercent.append(len(gc.stations[i].ebike)/gc.stations[i].ebike_cap)

import matplotlib.pyplot as plt
plt.hist(percent,bins=99,range=(0,1))
plt.xlabel('number of bike / capacity of bike station')
plt.ylabel('frequency')
plt.title('the distribution of bikes initial')
plt.xlim(0,1)
plt.savefig('the distribution of bikes initial',dpi=300)

#

plt.hist(epercent,bins=99,range=(0,1))
plt.xlabel('number of ebike / capacity of ebike docks')
plt.ylabel('frequency')
plt.title('the distribution of ebikes initial')
plt.xlim(0,1)
plt.savefig('the distribution of ebikes initial',dpi=300)


len(gc.bike_return_full)
len(gc.ebike_return_full)
len(gc.three_trip_error)
len(gc.demandlost)



def simulate(start_time,end_time,initial_stations, times):
    bike_return_full=[]
    ebike_return_full=[]
    three_trip_error=[]
    demandlost=[]
    for itera in range(times):
        print(itera)
        gc=SimData.GlobalClock(start_time,end_time,initial_stations)
        gc.clockAdvance()
        bike_return_full.append(len(gc.bike_return_full))
        ebike_return_full.append(len(gc.ebike_return_full))
        three_trip_error.append(len(gc.three_trip_error))
        demandlost.append(len(gc.demandlost))
    
    return bike_return_full,ebike_return_full,three_trip_error,demandlost
        
bike_return_full,ebike_return_full,three_trip_error,demandlost=simulate(start_time,end_time,initial_stations,50)

with open('result_50_times.csv','w') as f:
    f.write('bike_return_full,ebike_return_full,three_trip_error,demandlost\n')
    for i in range(50):
        f.write(str(bike_return_full[i])+',')
        f.write(str(ebike_return_full[i])+',')
        f.write(str(three_trip_error[i])+',')
        f.write(str(demandlost[i])+'\n')
    

with open('three_trip_error.csv','w') as f:
    f.write('bike,start_time,end_time,start_st,end_st\n')
    for i in  gc.three_trip_error:
        f.write(str(i.bike)+','+str(i.start_t)+','+str(i.end_t)+','+str(i.start_st)+','+str(i.end_st)+'\n')


with open('data/alltrips.csv','w') as f:
    f.write('bike,start_time,end_time,start_st,end_st\n')
    for i in  gc.trips:
        f.write(str(gc.trips[i].bike)+','+str(gc.trips[i].start_t)+','+str(gc.trips[i].end_t)+','+str(gc.trips[i].start_st)+','+str(gc.trips[i].end_st)+'\n')






class Event(object):

    # code
    START = 0
    END = 1
	# event1 = Event(Event.START, t, st)
    def __init__(self, code, time, station, tripid=None):
        
        self.time = time
        self.station = station
        self.code = code
        self.tripid = tripid
    ##
    # We are compared on 'time' field which is the next time
    # the simulation must process something
    ##
    def __lt__(self, other):
        return self.time < other.time
'''    
event1=Event(0,start_time,97)
event2=Event(0,start_time+td(seconds=1),97)
event3=Event(0,start_time+td(seconds=2),97)
import heapq
heap=[]
heapq.heappush(heap,event1)
heapq.heappush(heap,event2)
heapq.heappush(heap,event3)
'''