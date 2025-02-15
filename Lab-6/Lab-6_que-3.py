import datetime

date1=(1,12,2006)
date2=(11,2,2025)

date1=datetime.date(date1[2],date1[1],date1[0])
date2=datetime.date(date2[2],date2[1],date2[0])
d=date2-date1

print(d.days)