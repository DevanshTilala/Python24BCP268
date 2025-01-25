import time

current_time=int(time.strftime("%H"))

if(5 <= current_time < 12):
    print(f"Its {current_time} AM")
elif(12 <= current_time < 17):
    if current_time>12:
        current_time-=12
    print(f"Its {current_time} noon")
elif(17 <= current_time < 21):
    if current_time>12:
        current_time-=12
    print(f"Its {current_time} PM")
else:
    if current_time>12:
        current_time-=12
    print(f"Its {current_time} Midnight")