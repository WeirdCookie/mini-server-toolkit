import psutil
cpu_wert = psutil.cpu_percent(interval=1)
ram_wert = psutil.virtual_memory().percent
print(cpu_wert)
print(ram_wert)
