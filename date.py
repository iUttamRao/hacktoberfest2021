date=int(input("Enter the date"))
month=0
copy=date
day=0
year=0
r=0

def year_fun():
    year=date%10000
    return year

def day_fun(date):
    for i in range(1,5):
        date=date//10
    if date<10:   
        day=date%10
    else:
        day=date%100
    return day

def month_fun(copy):
    for i in range(1,7):
        copy=copy//10
    
    return copy

#print('MOnth :',month_fun(copy))
#print('Day :',day_fun(date))
#print('Year :',year_fun())

Month=month_fun(copy)
if Month==1:
    Month='January'
elif Month==2:
    Month='Fabruary'
elif Month==3:
    Month='March'
elif Month==4:
    Month='April'
elif Month==5:
    Month='May'
elif Month==6:
    Month='June'
elif Month==7:
    Month='July'
elif Month==8:
    Month='August'
elif Month==9:
    Month='September'
elif Month==10:
    Month='October'
elif Month==11:
    Month='November'
else:
    Month='December'

print(f'{Month} {day_fun(date)},{year_fun()}')
