import psutil

def get_cpu_temp():
    t = psutil.sensors_temperatures()
    for x in ['cpu-thermal', 'cpu_thermal']:
        if x in t:
            return t[x][0].current
    print("Warning: Unable to get CPU temperature!")
    return 0 
print(get_cpu_temp())