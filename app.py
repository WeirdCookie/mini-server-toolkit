import psutil
cpu_wert = psuitil.cpu_percent(interval=1)
ram_wert = psuitil.virtual_memory().cpu_percent
print(cpu_wert)
print(ram_wert)
