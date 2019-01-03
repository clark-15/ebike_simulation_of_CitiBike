allocation={}
travel_matrix={}
lambda_rate={}
for i in range(24):
    for j in range(7):
        allocation[i,j]=eval(open(('matrix_data/allocation_'+str(i)+'_'+str(j)+'.txt')).read())
        travel_matrix[i,j]=eval(open(('matrix_data/dest_matrix_'+str(i)+'_'+str(j)+'.txt')).read())
        lambda_rate=eval(open(('matrix_data/demand_ratio.txt')).read())


a = set()
for i in range(24):
    for j in range(7): 
        for m,n in allocation[i,j].items():
            a.add(m)
len(a)


b = set()
for i in range(24):
    for j in range(7): 
        for m,n in travel_matrix[i,j].items():
            for k,l in n.items():
                if k not in a:
                    b.add(k)
b

a=a.union(b)
closest=eval(open(('closest_bike_station.txt')).read())
station_rankby_dist=eval(open(('data/station_rankby_dist.txt')).read())
station_rankby_dist[3300][0]

c= set()
for i,j in closest.items():
    if j != station_rankby_dist[i][0]:
        c.add(i)

len(c)


len(closest)

d= set()
for i,j in closest.items():
    if i  in st :
        if j not in st:
            print(j)
            
            
            for k in station_rankby_dist[i]:
                if k in st:
                    closest[i] = k
                    break
   
tmp =  list( closest.keys())
for i in tmp:
    if i not in st:
        del closest[i]
len(closest)  
        


e=set()

for i,j in station_rankby_dist.items():
    if i in a:
        if j[0] not in a:
            print(j[0])
            e.add(j[0])
len(e)


initial_stations=eval(open(("stations_initial.txt")).read())
st = list(initial_stations.keys())
for i in st:
    if i not in g:
        del initial_stations[i]


        
len(initial_stations)

with open('stations_initial_751.txt','w') as f:
    f.write(str(initial_stations))
    
    
with open('closest_bike_station_751.txt','w') as f:
    f.write(str(closest))
    
    
len(e)
g= a.union(e)
len(f)
len()
st = g

len(station_rankby_dist)


tot = 0
for i,j in station_rankby_dist.items():
    tot += len(j)
tot


for i,j in station_rankby_dist.items():
    oo = j
    for p in oo:
        if p not in g:
            j.remove(p)


with open('data/station_rankby_dist_751.txt','w') as f:
    f.write(str(station_rankby_dist))
    
    
    