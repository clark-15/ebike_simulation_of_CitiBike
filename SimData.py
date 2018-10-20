'''
module to define the useful data structures in bike-sharing simulation
'''


'''
Event is either startTrip or endTrip
'''

import heapq
import numpy as np
from datetime import timedelta as td
#from datetime import datetime as time
allocation={}
travel_matrix={}
lambda_rate={}
for i in range(24):
    for j in range(7):
        allocation[i,j]=eval(open(('matrix_data/allocation_'+str(i)+'_'+str(j)+'.txt')).read())
        travel_matrix[i,j]=eval(open(('matrix_data/dest_matrix_'+str(i)+'_'+str(j)+'.txt')).read())
        lambda_rate=eval(open(('matrix_data/demand_ratio.txt')).read())

closest=eval(open(('closest_bike_station.txt')).read())
station_rankby_dist=eval(open(('data/station_rankby_dist.txt')).read())

import csv
bst={}
with open('data/bike_pair_traveltime_3000_for_NA.csv') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        bst[int(row[0]),int(row[1])]=float(row[2])
        
        

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

class Trip(object):
    def __init__(self, bike_id, start_time, end_time, start_st, end_st,start_SOC=None,end_SOC=None):
        self.tripid=str(start_time)+'_'+str(bike_id)
        self.bike = bike_id
        self.start_t = start_time
        self.end_t = end_time
        self.start_st = start_st
        self.end_st = end_st
        self.start_SOC=start_SOC
        self.end_SOC=end_SOC
##
# Class to handle a bike
##
class Bike(object):
    # bike status code
    
    def __init__(self, id, stationid,isebike,trip_times=0):
        #if trip_times = 2, the last trial 
        self.id = id
        self.isebike = isebike
        self.stationid = stationid 

        self.SOC = 100 if isebike else 0
        self.lastchargetime = -20
        self.last_chargeSOC=100
        self.trip_times=trip_times

class Station(object):

    def __init__(self, sid=None, bike = {}, ebike = {}, bike_cap=None, ebike_cap=None):
        self.sid = sid
        self.bike = bike
        self.ebike = ebike
        self.bike_cap = bike_cap
        self.ebike_cap = ebike_cap

        #self.tripsOut = []
        #self.tripsIn = []
        #self.tripsFailedOut = []
        #self.tripsFailedIn = []

class GlobalClock(object):

    '''
    records the simulation
    '''
    #  minimum interval time : 0.4608848028037159
    demand_rate=0.4608848028037159
    # thinning method, it can be time-varying
    #lambda_rate = 0.16930832461285625
    def __init__(self, start_time,end_time, initial_stations):

        self.start_time = start_time
        self.end_time=end_time
        self.t = start_time
        self.heap = []
        #self.tripGen = tripGenerator
        self.trips = {}
        self.bikes = {}
        self.stations = {}
        self.imagecount = 0
        self.demandlost=0
        self.demandlost_causedby_battery=0
        self.three_trip_error=[]
        self.bike_return_full=0
        self.ebike_return_full=0
        self.week = 0
        self.week_demandlost={}
        self.week_demandlost_causedby_battery={}
        self.week_three_trip_error={}
        self.week_bike_return_full={}
        self.week_ebike_return_full={}
        self.week_out_of_battery={}
        self.week_demandlost[0]=0
        self.week_three_trip_error[0]=0
        self.week_bike_return_full[0]=0
        self.week_ebike_return_full[0]=0
        self.week_out_of_battery[0]=0
        self.week_average_SOC = {}
        self.threshold = 30
        self.charge_rate=0.009259259
        self.energy_per_second=0.01984127
        self.out_of_battery = 0
        self.week_num_etrip={}
        self.week_num_etrip[0]=0
        self.num_etrip=0
        self.week_num_alltrip={}
        self.week_num_alltrip[0]=0
        self.week_average_SOC[0]=100
        self.week_demandlost_causedby_battery[0]=0
                
        self.weeks={}
        for i in range(100):
            self.weeks[i]=False
        
        
        for i in initial_stations.keys():
            bikelist={}
            ebikelist={}
            for bikeid in range(0,initial_stations[i]['bike']):
                bid=str(i)+'_'+str(bikeid)
                bike=Bike(bid,i,False)
                bikelist[bid]=bike
                self.bikes[bid]=bike
            for ebikeid in range(0,initial_stations[i]['ebike']):
                ebid='e_'+str(i)+'_'+str(ebikeid)
                ebike=Bike(ebid,i,True)
                ebikelist[ebid]=ebike
                self.bikes[ebid]=ebike
            station=Station(i,bikelist,ebikelist,initial_stations[i]['cap'],initial_stations[i]['ecap'])
            self.stations[i]=station
        self.sum_e,self.sum_b = 0,0
        for ei in self.bikes.keys():
            if self.bikes[ei].isebike==True:
                self.sum_e += 1
            else:
                self.sum_b += 1
        print('the total number of ebikes:',self.sum_e)
        print('the total number of regular bikes:',self.sum_b)
        Origin_generate(self,)
        
        
    def clockAdvance(self,):
        #print('start simulation')
        while(self.t <= self.end_time):
            next_event=heapq.heappop(self.heap)
            self.t=next_event.time
            #print(self.t)
            #print('day:',(self.t- self.start_time).days)
            #print('week: ',self.week)
            if (self.t- self.start_time).days % 7==0:
                self.week = ((self.t- self.start_time).days // 7)
                if self.weeks[self.week]==False:
                    #print((self.t- self.start_time).days)
                    print(self.t,self.week)
                    self.week_demandlost[self.week+1]=self.demandlost-sum(self.week_demandlost.values())
                    self.week_three_trip_error[self.week+1]=len(self.three_trip_error)-sum(self.week_three_trip_error.values())
                    self.week_bike_return_full[self.week+1]=self.bike_return_full-sum(self.week_bike_return_full.values())
                    self.week_ebike_return_full[self.week+1]=self.ebike_return_full-sum(self.week_ebike_return_full.values())
                    self.week_out_of_battery[self.week+1]=self.out_of_battery-sum(self.week_out_of_battery.values())
                    self.week_num_etrip[self.week+1]=self.num_etrip-sum(self.week_num_etrip.values())
                    self.week_num_alltrip[self.week+1]=len(self.trips)-sum(self.week_num_alltrip.values())
                    self.week_demandlost_causedby_battery[self.week+1]=self.demandlost_causedby_battery-sum(self.week_demandlost_causedby_battery.values())
                    self.weeks[self.week]= True
                    total_SOC = 0
                    for ei in self.bikes.keys():
                        if self.bikes[ei].isebike==True:
                             total_SOC += self.bikes[ei].SOC
                    self.week_average_SOC[self.week+1]=  total_SOC/self.sum_e
                    
                
            
            if next_event.code ==0: # means start
                trip_generate(self,next_event)
                Origin_generate(self,)
            elif next_event.code ==1: # means end
                return_generate(self,next_event)
                
            
        
        
        



def Origin_generate(globalclock):
    gc=globalclock
    Isgenerate=False
    start_t = gc.t
    while(Isgenerate==False):
        delta_t=td(seconds=np.random.exponential(gc.demand_rate))
        start_t += delta_t
        week_day=start_t.weekday()
        flip=int(np.random.binomial(1,lambda_rate[start_t.hour,week_day],1))
        if flip==1:
            Isgenerate=True
            origin=int(np.random.choice(list(allocation[start_t.hour,week_day].keys()),1,True,list(allocation[start_t.hour,week_day].values())))
            event=Event(Event.START,start_t,origin)
            heapq.heappush(gc.heap,event)
                
       
            
            
def trip_generate(globalclock,next_event):
    stationid=next_event.station
    gc=globalclock
    charge_rate=gc.charge_rate
    ebike_avaliable=False
    ebikeid=''
    #update SOC
    for j in gc.stations[stationid].ebike.keys():
        if gc.bikes[j].SOC < 100:
            #print(gc.t,j,gc.bikes[j].SOC,end=' -> ')
            new_SOC=gc.bikes[j].last_chargeSOC +(gc.t-gc.bikes[j].lastchargetime).seconds*charge_rate
            gc.bikes[j].SOC=min(100,new_SOC)
            
            
            #if gc.bikes[j].SOC < 30:
                #print(gc.t,j,gc.bikes[j].SOC)
            #print(gc.bikes[j].SOC)
        
    for j in gc.stations[stationid].ebike.keys():
        if gc.stations[stationid].ebike[j].SOC > gc.threshold:
            ebike_avaliable = True
            ebikeid=gc.stations[stationid].ebike[j].id
            break
    week_day=gc.t.weekday()
    dest=int(np.random.choice(list(travel_matrix[gc.t.hour,week_day][stationid].keys()),1,True,list(travel_matrix[gc.t.hour,week_day][stationid].values())))
    if len(gc.stations[stationid].bike) ==0 and ebike_avaliable==False:
        #gc.stations[stationid].tripsFailedOut.append(next_event)
        #gc.demandlost.append(next_event)
        gc.demandlost += 1
        if len(gc.stations[stationid].ebike)>0:
            gc.demandlost_causedby_battery += 1
        
    elif ebike_avaliable==False: # demand is bike
        generate_bike_trip(gc,stationid,dest)       
        
        
    else:# len(gc.stations[stationid].bike) ==0: # demand is ebike
        generate_ebike_trip(gc,stationid,dest,ebikeid)
        gc.num_etrip += 1
   
    


def generate_bike_trip(globalclock,stationid,dest,bikeid=None):
    gc=globalclock
    if bikeid == None:
        #print(stationid)
        #print(len(gc.stations[stationid].bike))
        bid, bike = gc.stations[stationid].bike.popitem()
    else:
        bid = bikeid
    bikingtime=bst[stationid,dest]
    sigma = 0.2571 # sqrt of 0.0661117309208
    duration=td(seconds=bikingtime*np.random.lognormal(0,sigma))
    end_time=gc.t+duration
    trip=Trip(bid,gc.t,end_time,stationid,dest)
    #print(trip)
    #print(trip.tripid)
    gc.trips[trip.tripid]=trip
    #gc.stations[stationid].tripsOut.append(trip)
    event=Event(Event.END,end_time,dest,trip.tripid)
    heapq.heappush(gc.heap,event)
    
def generate_ebike_trip(globalclock,stationid,dest,ebikeid,pickupebike=True):
    gc=globalclock
    bikingtime=bst[stationid,dest]
    slow_ratio=2.25 # if the battery run out of, the speed is 1/2.25 times the ebike speed
    #print(stationid,ebikeid)
    if pickupebike:
        del gc.stations[stationid].ebike[ebikeid]
        
    sigma = 0.2571 # sqrt of 0.0661117309208
    speed_ratio=2/3
    duration=td(seconds=bikingtime*np.random.lognormal(0,sigma)*speed_ratio)
    
    
    energy_per_second=gc.energy_per_second # SOC / second
    energy=duration.total_seconds()*energy_per_second
    remaining_battery=gc.bikes[ebikeid].SOC-energy
    
    if remaining_battery>0:
        end_time=gc.t+duration
        end_SOC=remaining_battery
    else:
        gc.out_of_battery += 1
        end_SOC=0
        end_time=gc.t+gc.bikes[ebikeid].SOC/energy*duration+(-remaining_battery)/energy*duration*slow_ratio
        
    trip=Trip(ebikeid,gc.t,end_time,stationid,dest,gc.bikes[ebikeid].SOC,end_SOC)
    gc.bikes[ebikeid].SOC=end_SOC
    gc.trips[trip.tripid]=trip
    #gc.stations[stationid].tripsOut.append(trip)
    event=Event(Event.END,end_time,dest,trip.tripid)
    heapq.heappush(gc.heap,event)
    
def return_generate(globalclock,next_event):
    gc=globalclock
    stationid=next_event.station
    tripid=next_event.tripid
    bid=gc.trips[tripid].bike
    if gc.bikes[bid].isebike:
        return_ebike(gc,tripid,stationid)
    else:
        return_bike(gc,tripid,stationid)





def return_ebike(globalclock,tripid,stationid):
    gc=globalclock
    ebikeid=gc.trips[tripid].bike
    if len(gc.stations[stationid].ebike) < gc.stations[stationid].ebike_cap :
        gc.stations[stationid].ebike[ebikeid]=gc.bikes[ebikeid]
        #gc.bikes[ebikeid].SOC=100
        gc.bikes[ebikeid].lastchargetime=gc.t
        #gc.stations[stationid].tripsIn.append(gc.trips[tripid])
        gc.bikes[ebikeid].trip_times=0
        gc.bikes[ebikeid].last_chargeSOC=gc.bikes[ebikeid].SOC
    else:
        gc.ebike_return_full += 1
        #gc.stations[stationid].tripsFailedIn.append(gc.trips[tripid])
        if gc.bikes[ebikeid].trip_times > 2:
            gc.three_trip_error.append(gc.trips[tripid])
            #print(gc.t,'three')
            # immediately return
            for return_dest in station_rankby_dist[stationid]:
                if len(gc.stations[return_dest].ebike) < gc.stations[return_dest].ebike_cap:
                    dest=return_dest
                    break
            gc.stations[dest].ebike[ebikeid]=gc.bikes[ebikeid]
            #gc.bikes[ebikeid].SOC=100
            gc.bikes[ebikeid].lastchargetime=gc.t
            gc.bikes[ebikeid].trip_times=0
            gc.bikes[ebikeid].last_chargeSOC=gc.bikes[ebikeid].SOC
        else:
            gc.bikes[ebikeid].trip_times += 1
            #print(station_rankby_dist[stationid])
            for next_dest in station_rankby_dist[stationid]:
                #print(ebikeid,next_dest)
                if len(gc.stations[next_dest].ebike) < gc.stations[next_dest].ebike_cap:
                    dest=next_dest
                    break
            generate_ebike_trip(gc,stationid,dest,ebikeid,pickupebike=False)
            gc.num_etrip += 1
        
        
def return_bike(globalclock,tripid,stationid):
    gc=globalclock
    bikeid=gc.trips[tripid].bike
    if len(gc.stations[stationid].bike) < gc.stations[stationid].bike_cap :
        gc.stations[stationid].bike[bikeid]=gc.bikes[bikeid]
        #gc.stations[stationid].tripsIn.append(gc.trips[tripid])
        gc.bikes[bikeid].trip_times=0
        
    else:
        gc.bike_return_full += 1
        #gc.stations[stationid].tripsFailedIn.append(gc.trips[tripid])
        if gc.bikes[bikeid].trip_times > 2:
            gc.three_trip_error.append(gc.trips[tripid])
            #print(gc.t,'three')
            # immediately return
            for return_dest in station_rankby_dist[stationid]:
                if len(gc.stations[return_dest].bike) < gc.stations[return_dest].bike_cap:
                    dest=return_dest
                    break
            gc.stations[dest].bike[bikeid]=gc.bikes[bikeid]
            gc.bikes[bikeid].trip_times=0
        else:
            gc.bikes[bikeid].trip_times += 1
            for next_dest in station_rankby_dist[stationid]:
                if len(gc.stations[next_dest].bike) < gc.stations[next_dest].bike_cap:
                    dest=next_dest
                    break
            generate_bike_trip(gc,stationid,dest,bikeid)
            
    

