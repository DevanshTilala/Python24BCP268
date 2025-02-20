employee={(1,101):10000,(1,102):20000,
          (2,101):5000,(2,102):30000,
          (3,101):25000,(3,102):20000}
employee1={}

for (dept, _),salary in employee.items():
    if dept not in employee1:
        employee1[dept]={"min": salary, "max": salary}
    else:
        employee1[dept]['min']=min(employee1[dept]['min'], salary)
        employee1[dept]['max']=max(employee1[dept]['max'], salary)

print(employee1)