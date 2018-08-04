import pandas as pd
from threading import Thread
#import tbb
from geopy.distance import great_circle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from math import radians, cos, sin, asin, sqrt
def lati_longi(loc):
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
    return lat_long[loc]
def datasets1(tym,v1,v2,v3,v4,loc):
    path="datasets1.csv"
    data = pd.read_csv(path)
    model = RandomForestRegressor()
    predictors = np.array(['Time_interval', 'Kothamangalam','Mathirappilly','Karukadam','Puthuppady'])
    y = data.Average_speed
    X = data[predictors]
    model.fit(X, y)
    d = [[tym, v1, v2, v3, v4]]
    l = lati_longi(loc)
    g = lati_longi('Muvattupuza')
    dist =great_circle(tuple(l),tuple(g)).kilometers
    print(dist)
    print(dist / model.predict(d))
def datasets2(tym,v1,v2,v3,v4,loc):
    path="datasets2.csv"
    data=pd.read_csv(path)
    model = RandomForestRegressor()
    predictors = np.array(['Time_interval', 'Vazhakulam','Avoly','Anicadu','Kizhakkekara'])
    y=data.Average_speed
    X = data[predictors]
    model.fit(X, y)
    d=[[tym,v1,v2,v3,v4]]
    l = lati_longi(loc)
    g = lati_longi('Muvattupuza')
    dist = great_circle(tuple(l),tuple(g)).kilometers
    print(dist)
    print(dist/model.predict(d))
def datasets3(tym,v1,v2,loc):
    path="datasets3.csv"
    data = pd.read_csv(path)
    model = RandomForestRegressor()
    predictors = np.array(['Time_interval', 'Arakuzha','Perumballoor'])
    y = data.Average_speed
    X = data[predictors]
    model.fit(X, y)
    d = [[tym,v1,v2]]
    l = lati_longi(loc)
    g = lati_longi('Muvattupuza')
    dist = great_circle(tuple(l),tuple(g)).kilometers
    print(dist)
    print(dist / model.predict(d))
data1=Thread(target=datasets1(3,34,52,45,12,'Kothamangalam'))
data2=Thread(target=datasets2(1,23,55,33,55,'Vazhakulam'))
data3=Thread(target=datasets3(1,45,34,'Arakuzha'))
data1.start()
data2.start()
data3.start()
data1.join()
data2.join()
data3.join()