# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 13:47:07 2018

@author: liumo
"""

import pandas as pd
import csv
bst={}
with open('data/bike_pair_traveltime.csv') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        bst[int(row[1]),int(row[2])]=float(row[3])

with open('bike_pair_traveltime_3000_for_NA.csv','w') as f:
    f.write('ori,dest,duration\n')
    for i in stationlist:
        for j in stationlist:
            if (i,j) in bst.keys():
                f.write(str(i)+','+str(j)+','+str(bst[i,j])+'\n')
            else:
                f.write(str(i)+','+str(j)+',3000\n')

stationlist=set()
for i,j in bst.keys():
    stationlist.add(i)
    stationlist.add(j)
len(stationlist) 
stationlist=list(sorted(stationlist))   
stationlist[0]
closest={}
dist={}    
for i in stationlist:
    for j in stationlist:
        if (i,j) in bst.keys():
            if i not in closest.keys():
                closest[i]=j
                dist[i]=bst[i,j]
            elif dist[i] > bst[i,j]:
                closest[i]=j
                dist[i]=bst[i,j]
            if j not in closest.keys():
                closest[j]=i
                dist[j]=bst[i,j]
            elif dist[j] > bst[i,j]:
                closest[j]=i
                dist[j]=bst[i,j]
                
                
                
                
f = open("closest_bike_station.txt","w")
f.write( str(closest) )
f.close()                        


closest=eval(open(('closest_bike_station.txt')).read())

missing=[]
for i in stationlist:
    for j in stationlist:
        if (i,j) not in bst.keys():
            missing.append((i,j))
            
            
missingstationlist=set()
for (i,j) in missing:
    missingstationlist.add(i)
    missingstationlist.add(j)
    
len(missingstationlist)
    
sum(bst.values())/len(bst)            

#use 3000 to replace the missing data

f = open("bike_station_time.txt","w")
f.write( str(bst) )
f.close()

duration=eval(open(('bike_station_time.txt')).read())
closest=eval(open(('closest_bike_station.txt')).read())
cap={}
with open('bikestationcap.csv') as f:
    reader=csv.reader(f) 
    for row in reader:
        cap[int(row[0])]=int(row[1])                   
num_bike_each_station={}
num_ebike_each_station={}
ecap={}
for i in cap.keys():
    num_bike_each_station[i]=round(cap[i]*0.5)
    ecap[i]=round(cap[i]*0.2)
    num_ebike_each_station[i]=round(cap[i]*0.05)
    
cap
ecap            
num_ebike_each_station
           
f = open("bikestationcap.txt","w")
f.write( str(cap) )
f.close()
f = open("bikestation_ecap.txt","w")
f.write( str(ecap) )
f.close()
f = open("initial_bike.txt","w")
f.write( str(num_bike_each_station) )
f.close()
f = open("initial_ebike.txt","w")
f.write( str(num_ebike_each_station) )
f.close()

allocation_dis={}
for i in stationlist:
    if i not in al.index:
        print(i)
        allocation_dis[i]=0
    else:
        allocation_dis[i]=al.loc[i,'allocation']
    
    
    
travel={}
for i in cap.keys():
    for j in cap.keys():
        travel[i,j]=1/len(cap)

f = open("allocation.txt","w")
f.write( str(allocation_dis) )
f.close()

f = open("travel_matrix.txt","w")
f.write( str(travel) )
f.close()

allocation=eval(open(('allocation.txt')).read())
allocation


stations={}
for i in cap.keys():
    temp={}
    temp['cap']=cap[i]
    temp['ecap']=ecap[i]
    temp['bike']=num_bike_each_station[i]
    temp['ebike']=num_ebike_each_station[i]
    stations[i]=temp
    
    
    
f = open("stations_initial.txt","w")
f.write( str(stations) )
f.close()

travel={}
for i in cap.keys():
    temp={}
    for j in cap.keys():
        temp[j]=1/len(cap)
    travel[i]=temp
        

import sched

import pandas as pd

citi5=pd.read_csv('../citibike-tripdata.csv/201706-citibike-tripdata.csv')
citi2=pd.read_csv('../citibike-tripdata.csv/201707-citibike-tripdata.csv')
citi3=pd.read_csv('../citibike-tripdata.csv/201708-citibike-tripdata.csv')
citi4=pd.read_csv('../citibike-tripdata.csv/201709-citibike-tripdata.csv')


citi5=citi5.append(citi2)
citi5=citi5.append(citi3)
citi5=citi5.append(citi4)
citi5=citi5.drop(columns=['tripduration',  'stoptime', 
       'start station name', 'start station latitude',
       'start station longitude',  'end station name',
       'end station latitude', 'end station longitude', 'bikeid', 'usertype',
       'birth year', 'gender'])
    
len(citi1)/30/4

#Out: 59681.575

citi1=citi5.reset_index()
citi1.to_csv('../citibike-tripdata.csv/before_delete.csv')
del citi1['index']
len(citi5) # 7161789


for i in range(len(citi1)):
    if i < 4776303:
        continue
    if (citi1.loc[i,'start'] not in stationlist) or \
    (citi1.loc[i,'end'] not in stationlist):
        citi1=citi1.drop(i)
    if i % 100000 == 0:
        print(i/7161789)
citi1.to_csv('../citibike-tripdata.csv/after_delete.csv')
citi1=pd.read_csv('../citibike-tripdata.csv/after_delete.csv')
len(citi1)
JCciti=pd.read_csv('../JC-citibike-tripdata/combine1.csv')
JCciti.columns=['starttime','start','end']
citi1.columns=['index','starttime','start','end']



del citi1['index']
citi=citi1.append(JCciti)

len(citi)/30/4
Out[107]: 60306.9


citi=citi.reset_index()
del citi['index']
citi.to_csv('combine_JC.csv')
citi1=citi
al=citi1.groupby('start').count()
total=sum(al['starttime'])
for i in al.index:
    al.loc[i,'allocation']=float(al.loc[i,'starttime']/total)
al.to_csv('allocation.csv')
citi1.columns=['starttime','start','end']  
travel={}  
for i in stationlist:
    print(i)
    if i not in al.index:
        print(i)
        continue
    temp={}
    k=citi1[citi1.start==i]
    k=k.groupby('end').count()
    if i not in k.index:
        total1=sum(k['start'])
    else:
        total1=sum(k['start'])-k.loc[i,'start']
    for j in stationlist:
        if j ==i:
            temp[j]=0
        elif j in k.index:
            temp[j]=k.loc[j,'start']/total1
        else:
            temp[j]=0
    travel[i]=temp


## demand rate
    
citi1
int(citi.loc[1000,'starttime'][11:13])

def weekDay(month, day):
    year=2017
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365                  
    # leap year correction    
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)             
    dayOfWeek %= 7
    
    return int(dayOfWeek)

weekDay(7,31)
# 0 is Sunday
with open('hours_combine_week.csv','a') as f:
    #f.write('week,starthours,start,destination\n')
    for i in range(len(citi)):
        if i < 7161746: continue
        if i < 7161746:
            month=int(citi.loc[i,'starttime'][5:7])
            day=int(citi.loc[i,'starttime'][8:10])
            f.write(str(weekDay(month,day))+',')
            f.write(str(int(citi.loc[i,'starttime'][11:13]))+',')
            f.write(str(citi.loc[i,'start'])+',')
            f.write(str(citi.loc[i,'end'])+'\n')
            
        else:
            month=int(citi.loc[i,'starttime'][5:6])
            day=int(citi.loc[i,'starttime'][7:9])
            f.write(str(weekDay(month,day))+',')
            f.write(str(int(citi.loc[i,'starttime'][-5:-3]))+',')
            f.write(str(citi.loc[i,'start'])+',')
            f.write(str(citi.loc[i,'end'])+'\n')
        if i % 100000 ==0:
            print(i/7236828)
    
    

hours=pd.read_csv('hours_combine_week.csv')
demand_interval={}
for i in range(24):
    hor=hours[hours.starthours==i]
    for weekday in range(7):
        #print(weekday)
        al={}
        dest_m={}
        day=hor[hor.week==weekday]
        interval=3600*4*4/len(day)
        demand_interval[i,weekday]=interval
        total=len(day)
        alloc=day.groupby('start').count()
        
        for station in alloc.index:
            al[station]=alloc.loc[station,'destination']/total
            start_m=day[day.start==station]
            dest_count=start_m.groupby('destination').count()
            total_dest=len(start_m)
            temp={}
            for dest in dest_count.index:
                temp[dest]=dest_count.loc[dest,'start']/total_dest
            dest_m[station]=temp
        print('finish counting, beging writing',i,weekday)
        f = open('allocation_'+str(i)+'_'+str(weekday)+'.txt',"w")
        f.write( str(al) )
        f.close()
        f = open('dest_matrix_'+str(i)+'_'+str(weekday)+'.txt',"w")
        f.write( str(dest_m) )
        f.close()

f = open('demand_rate.txt',"w")
f.write( str(demand_interval) )
f.close()    
                
    
import matplotlib.pyplot as plt
interval=eval(open(('../demand_rate.txt')).read())
mini=min(interval.values())
rate={}
for i,j in interval.keys():
    rate[i,j]=mini/interval[i,j]

f = open('data/demand_ratio.txt',"w")
f.write( str(rate) )
f.close()   



week   = ['Sunday', 
              'Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday',  
              'Friday', 
              'Saturday']
i = 6
demand_day=[]
for j in range(24):
    demand_day.append(1/rate[j,i]*3600)
plt.plot(demand_day)
plt.scatter(range(24),demand_day)
plt.ylabel('number of demand in one hour')
plt.xlabel('time')
plt.title('demand rate on '+str(week[i]))
plt.xticks(range(24))
plt.savefig('data/demand rate on '+str(week[i]),dpi=300)



sum(dest_m[3635].values())


len(hour[(hour.starttime==0)|(hour.starttime==1)|(hour.starttime==2)|(hour.starttime==3)|(hour.starttime==4)|(hour.starttime==5)\
     |(hour.starttime==6)|(hour.starttime==23)|(hour.starttime==22)]  )
# 94881
9*3600*4*30/96881    # 40.13170797163531

len(hour)-94881
#     953694
15*3600*4*30/953694 # 6.794632240529982

6.794632240529982/40.13170797163531

rate=[]
for i in range(24):
    rate.append(3600*4*30/len(hour[hour.starttime==i]))


rate=[]
for i in range(24):
    rate.append(len(hour[hour.starttime==i])/(4*30))
    
    
import matplotlib.pyplot as plt
plt.plot(rate)
plt.scatter(range(24),rate)
plt.ylabel('number of demand in one hour')
plt.xlabel('time')
plt.title('demand rate in one day')
plt.xticks(range(24))
plt.savefig('demand rate in one day',dpi=300,bbox_inches='tight')






import csv
bst={}
with open('data/bike_pair_traveltime_3000_for_NA.csv') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        bst[int(row[0]),int(row[1])]=float(row[2])

station_rankby_dist={}        
for station in stationlist:
    temp={}
    for i, j in bst:
        if i==station:
          temp[j]=bst[i,j]
    rank=sorted(temp,key=temp.get)
    station_rankby_dist[station]=rank
    print(station)
f = open('data/station_rankby_dist.txt',"w")
f.write( str(station_rankby_dist) )
f.close()   

