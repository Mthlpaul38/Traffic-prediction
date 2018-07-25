import csv
with open('datasets2.csv', 'w') as csvfile:
    fieldnames = ['Time_interval', 'Vazhakulam','avoly','Nirmala','adooparambu','Reach_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    places={"Vazhakulam","avoly","Nirmala","adooparambu"}
    Time_interval={1,2,3,4,5}
    interval={"22:00-7:00","7:00-10:00","10:00-16:00","16:00-19:00","19:00-22:00"}
    for i in Time_interval:
        if i==1:
            for j in range(30,41,5):
                for k in range(j+30,j+41,5):
                    writer.writerow({'Time_interval':i, 'Vazhakulam':j,'avoly':k,'Nirmala':k,'adooparambu':k,'Reach_time':7.6/k+1/j})
        if i==2:
            for j in range(20,31,5):
                for k in range(j+30,j+51,5):
                    for l in range(20,31,5):
                        for m in range(30,41,5):
                            writer.writerow(
                                {'Time_interval': i, 'Vazhakulam': j, 'avoly': k, 'Nirmala': l, 'adooparambu': m,
                                 'Reach_time': 7.2 / k + 1 / j+.2/l+.2/m})
        if i==3:
            for j in range(20,31,5):
                for k in range(j+30,j+51,5):
                    for l in range(40,70,5):
                        for m in range(30,50,5):
                            writer.writerow(
                                {'Time_interval': i, 'Vazhakulam': j, 'avoly': k, 'Nirmala': l, 'adooparambu': m,
                                 'Reach_time': 7.2 / k + 1 / j+.2/l+.2/m})
        if i==4:
            for j in range(20,31,5):
                for k in range(j+30,j+51,5):
                    for l in range(20,26,5):
                        for m in range(20,36,5):
                            writer.writerow(
                                {'Time_interval': i, 'Vazhakulam': j, 'avoly': k, 'Nirmala': l, 'adooparambu': m,
                                 'Reach_time': 7.2 / k + 1 / j+.2/l+.2/m})
        if i==5:
            for j in range(20,31,5):
                for k in range(j+30,j+51,5):
                    for l in range(40,60,5):
                        for m in range(30,60,5):
                            writer.writerow(
                                {'Time_interval': i, 'Vazhakulam': j, 'avoly': k, 'Nirmala': l, 'adooparambu': m,
                                 'Reach_time': 7.2 / k + 1 / j+.2/l+.2/m})










