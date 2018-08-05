import pandas as pd
from threading import Thread,Lock
#import tbb
import time
from geopy.distance import great_circle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
lock=Lock()
def zone(hr,min,sec):
    if(min==0 and hr==7):
        z=1
    elif(min==0 and hr==10):
        z=2
    elif(min==0 and hr==16):
        z=3
    elif(min==0 and hr==19):
        z=4
    elif(min==0 and hr==22):
        z=5
    else:
        if( hr>=7 and hr<10 and min>0):
            z=2
        elif( hr>=10 and hr<16 and min>0):
            z=3
        elif( hr>=16 and hr<19 and min>0):
            z=4
        elif( hr>=19 and hr<22 and min>0):
            z=5
        else:
            z=1
    return z
def lati_longi(loc):
    lock.acquire()
    lat_long = {'Kothamangalam': [10.060190, 76.635083],
                'Mathirappilly': [10.045843, 76.616721],
                'Karukadam': [10.033244, 76.609500],
                'Puthuppady': [10.011139, 76.603722],
                'Vazhakulam': [9.946958, 76.635900],
                'Avoly': [9.958699, 76.625166],
                'Anicdu': [9.968679, 76.607780],
                'Kizhakkekara': [9.977876, 76.592166],
                'Muvattupuza': [9.989423, 76.578975],
                'Arakuzha': [9.927757, 76.602278],
                'Perumballoor': [9.953572, 76.592763]
                }
    lock.release()
    return lat_long[loc]
def datasets1(tym,loc):
    path="datasets1.csv"
    places1 = ['Kothamangalam','Mathirappilly','Karukadam','Puthuppady']
    n = places1.index(current_loc)
    places1 = places1[n:]
    v=[]
    for i in places1:
        print("speed at place", i)
        x = int(input())
        v.append(x)
    data = pd.read_csv(path)
    model = RandomForestRegressor()
    l = ['Time_interval']+places1
    predictors =np.array(l)
    y = data.Average_speed
    X = data[predictors]
    model.fit(X, y)
    d=[tym]
    for j in v:
        d.append(j)
    l = lati_longi(loc)
    g = lati_longi('Muvattupuza')
    dist =great_circle(l,g).kilometers
    return (dist / model.predict([d]))
def datasets2(tym,loc):
    path="datasets2.csv"
    places2 = ['Vazhakulam', 'Avoly', 'Anicadu', 'Kizhakkekara']
    data=pd.read_csv(path)
    n = places2.index(current_loc)
    places2 = places2[n:]
    v = []
    for i in places2:
        print("speed at place",i)
        x=int(input())
        v.append(x)
    model = RandomForestRegressor()
    l = ['Time_interval'] + places2
    predictors = np.array(l)
    y=data.Average_speed
    X = data[predictors]
    model.fit(X, y)
    d = [tym]
    for j in v:
        d.append(j)
    l = lati_longi(loc)
    g = lati_longi('Muvattupuza')
    dist = great_circle(tuple(l),tuple(g)).kilometers
    return dist/model.predict([d])
def datasets3(tym,v1,v2,loc):
    path="datasets3.csv"
    data = pd.read_csv(path)
    model = RandomForestRegressor()
    places3 = ["Arakuzha", "Perumballoor"]
    n = places3.index(current_loc)
    places3 = places3[n:]
    v = []
    for i in places3:
        print("speed at place", i)
        x = int(input())
        v.append(x)
    l = ['Time_interval'] + places3
    predictors = np.array(l)
    y = data.Average_speed
    X = data[predictors]
    model.fit(X, y)
    d = [tym]
    for j in v:
        d.append(j)
    l = lati_longi(loc)
    l = lati_longi(loc)
    g = lati_longi('Muvattupuza')
    dist = great_circle(tuple(l),tuple(g)).kilometers
    return dist / model.predict([d])
places1=["Kothamangalam","Mathirappilly","Karukadam","Puthuppady"]
places2=['Vazhakulam','Avoly','Anicadu','Kizhakkekara']
places3=["Arakuzha","Perumballoor"]
current_loc=input("enter the current location")
dest=input("enter the destination")
if current_loc in places1:
    n=places1.index(current_loc)
    places1=places1[n:]
    t = time.strftime("%H:%M:%S")  # get system time
    hr = t[0] + t[1]
    hr = int(hr)
    min = t[3] + t[4]
    min = int(min)
    sec = t[6] + t[7]
    sec = int(sec)
    q = int(zone(hr, min, sec))
    tym=datasets1(q,current_loc)
elif current_loc in places2:
    t = time.strftime("%H:%M:%S")  # get system time
    hr = t[0] + t[1]
    hr = int(hr)
    min = t[3] + t[4]
    min = int(min)
    sec = t[6] + t[7]
    sec = int(sec)
    q = int(zone(hr, min, sec))
    tym=datasets2(q,current_loc)
else:
    t = time.strftime("%H:%M:%S")  # get system time
    hr = t[0] + t[1]
    hr = int(hr)
    min = t[3] + t[4]
    min = int(min)
    sec = t[6] + t[7]
    sec = int(sec)
    q = int(zone(hr, min, sec))
    tym=datasets3(q,23,56,current_loc)
print(tym[0])