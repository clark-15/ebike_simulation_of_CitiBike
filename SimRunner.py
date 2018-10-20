'''

the runner of simulation of ebikes

'''



import SimData
from datetime import timedelta as td
from datetime import datetime as time
start_time = time(2017,7,1,hour= 18)
end_time=start_time+ td(weeks=20)
initial_stations=eval(open(("stations_initial.txt")).read())



gc=SimData.GlobalClock(start_time,end_time,initial_stations)

gc.clockAdvance()

#import pickle
#gc=pickle.load(open('../gc_20weeks.pickle','rb'))




#-------analyze the result------------
time_hour=end_time
end_hour=time_hour+td(hours=1)

gc1=SimData.GlobalClock(time_hour,end_hour,stations_20weeks)

for hours in range(24):
    gc1.clockAdvance()
    with open(str(gc1.end_time.strftime('%m-%d-%Y_%H_%M_%S'))+'_bike.csv','w') as f:
        f.write('stationid,num_of_bike_dividedby_bike_capacity\n')
        for i in gc1.stations.keys():
            if gc1.stations[i].bike_cap != 0:
                f.write(str(i)+',')
                f.write(str(len(gc1.stations[i].bike)/gc1.stations[i].bike_cap)+'\n')
                
    with open(str(gc1.end_time.strftime('%m-%d-%Y_%H_%M_%S'))+'_ebike.csv','w') as f:
        f.write('stationid,num_of_ebike_dividedby_ebike_capacity\n')
        for i in gc1.stations.keys():
            if gc1.stations[i].ebike_cap != 0:
                f.write(str(i)+',')
                f.write(str(len(gc1.stations[i].ebike)/gc1.stations[i].ebike_cap)+'\n')
        
    gc1.end_time += td(hours=1)



num,enum=0,0
for i in gc.stations.keys():
    num += len(gc.stations[i].bike)
    enum += len(gc.stations[i].ebike)


# num: 12613

# enum: 1243
    
cap,ecap = 0,0
for i in gc.stations.keys():
    cap += gc.stations[i].bike_cap
    ecap += gc.stations[i].ebike_cap
cap/2 # 12657

ecap /2 # 2534.5 

len(gc.bikes)-num-enum

(len(gc.trips)-len(gc.bike_return_full)-len(gc.ebike_return_full))/140
len(gc.trips)/140
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
plt.title('the distribution of bikes 20 weeks')
plt.xlim(0,1)
plt.savefig('the distribution of bikes 20 weeks_recycle_bike',dpi=300)

#

plt.hist(epercent,bins=99,range=(0,1))
plt.xlabel('number of ebike / capacity of ebike docks')
plt.ylabel('frequency')
plt.title('the distribution of ebikes 20 weeks')
plt.xlim(0,1)
plt.savefig('the distribution of ebikes 20 weeks_recycle_bike',dpi=300)


len(gc.bike_return_full)
len(gc.ebike_return_full)
len(gc.three_trip_error)
len(gc.demandlost)

y=gc.week_demandlost.values()
s='lost demand (out-of-battery_delay)'
y=list(y)[2:]
x=range(1,len(y)+1)
#plt.xticks(x,x)
plt.scatter(x,y)
plt.plot(x,y)
plt.ylabel('number of '+str(s)+' in a week')
plt.xlabel('week')
plt.title('number of '+str(s)+' in a week VS week')
plt.savefig(s+'recycle_bike',dpi=300,bbox_inches='tight')




y=gc.week_three_trip_error.values()
s='three-trip-error (out-of-battery_delay)'
y=list(y)[2:]
x=range(1,len(y)+1)
#plt.xticks(x,x)
plt.scatter(x,y)
plt.plot(x,y)
plt.ylabel('number of '+str(s)+' in a week')
plt.xlabel('week')
plt.title('number of '+str(s)+' in a week VS week')
plt.savefig(s+'recycle_bike',dpi=300,bbox_inches='tight')






y=gc.week_bike_return_full.values()
s='bike return error (out-of-battery_delay)'
y=list(y)[2:]
x=range(1,len(y)+1)
#plt.xticks(x,x)
plt.scatter(x,y)
plt.plot(x,y)
plt.ylabel('number of '+str(s)+' in a week')
plt.xlabel('week')
plt.title('number of '+str(s)+' in a week VS week')
plt.savefig(s+'recycle_bike',dpi=300,bbox_inches='tight')




y=gc.week_ebike_return_full.values()
s='ebike return error (out-of-battery_delay)'
y=list(y)[2:]
x=range(1,len(y)+1)
#plt.xticks(x,x)
plt.scatter(x,y)
plt.plot(x,y)
plt.ylabel('number of '+str(s)+' in a week')
plt.xlabel('week')
plt.title('number of '+str(s)+' in a week VS week')
plt.savefig(s+'recycle_bike',dpi=300,bbox_inches='tight')


y1=list(gc.week_ebike_return_full.values())
y2=list(gc.week_bike_return_full.values())
y3=list(gc.week_demandlost.values())
y=list(map(lambda x,y,z: x+y+z , y1,y2,y3))
s='total unhappy event (out-of-battery_delay)'
y=list(y)[2:]
x=range(1,len(y)+1)
plt.xticks(x,x)
plt.scatter(x,y)
plt.plot(x,y)
plt.ylabel('number of '+str(s)+' in a week')
plt.xlabel('week')
plt.title('number of '+str(s)+' in a week VS week')
plt.savefig(s+'recycle_bike',dpi=300,bbox_inches='tight')


y=gc.week_average_SOC.values()
s='everage State of Charge(SOC)'
y=list(y)[2:]
x=range(1,len(y)+1)
plt.xticks(x,x)
plt.scatter(x,y)
plt.plot(x,y)
plt.ylabel('number of '+str(s)+' in a week')
plt.xlabel('week')
plt.title(str(s)+' in a week VS week')
plt.savefig(s+'recycle_bike',dpi=300,bbox_inches='tight')




SOC=[]
for ei in gc.bikes.keys():
    if gc.bikes[ei].isebike==True:
         SOC.append(gc.bikes[ei].SOC)




plt.hist(SOC,bins=99,range=(0,100),log=True)
plt.title('distribution of SOC after 40 weeeks')
plt.ylabel('number of bikes (log scaled)')
plt.xlabel('SOC')
plt.axvline(x=30,color='red')
plt.savefig('distribution of SOC after 20 weeeks',dpi=300,bbox_inches='tight')

len(SOC)


len(gc.trips)
outofbatterytrip=0
etrip = 0
for i in gc.trips.keys():
    if gc.trips[i].end_SOC != None:
        etrip += 1
    if gc.trips[i].end_SOC==0:
        outofbatterytrip += 1
        
etrip
etrip/len(gc.trips) 
outofbatterytrip/etrip

(gc.bike_return_full)/(len(gc.trips)-etrip)
(gc.ebike_return_full)/(etrip)

gc.demandlost/(len(gc.trips)+gc.demandlost)

# stateafter 20 weeks
from copy import deepcopy
stations_20weeks=deepcopy(initial_stations)
for i in gc.stations.keys():
    stations_20weeks[i]['bike']=len(gc.stations[i].bike)
    stations_20weeks[i]['ebike']=len(gc.stations[i].ebike)

import pickle
pickle.dump(stations_20weeks,open('stations_20weeks.pickle','wb'))

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
    f.write('bike,start_time,end_time,start_st,end_st,start_SOC,end_SOC\n')
    for i in  list(gc.trips.keys())[:200000]:
        if gc.trips[i].end_SOC != None:
            f.write(str(gc.trips[i].bike)+','+str(gc.trips[i].start_t)+','+str(gc.trips[i].end_t)+','+str(gc.trips[i].start_st)+','+str(gc.trips[i].end_st)+','+str(gc.trips[i].start_SOC)+','+str(gc.trips[i].end_SOC)+'\n')




