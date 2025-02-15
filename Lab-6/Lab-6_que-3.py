import datetime

def days_difference(d1,d2):
    d1=datetime.date(d1[2],d1[1],d1[0])
    d2=datetime.date(d2[2],d2[1],d2[0])
    
    return (d2-d1).days

date1=(1,12,2006)
date2=(11,2,2025)

print(f"Difference between two dates is {days_difference(date1,date2)}")