def hour24():
    for i in range(1,25):
        if i<=11:
            print(i,'AM')
        elif i==12:
            print(i,'AM is Mid-Day')
        elif i<=23:
            print(i,'PM')
        elif i==24:
            print(i,'PM is Mid-Night')
hour24()