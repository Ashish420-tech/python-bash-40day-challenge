import os

print("Load average:", os.getloadavg())

with open("/proc/meminfo") as f:
   for i in range(5):
       print(f.readline().strip())
