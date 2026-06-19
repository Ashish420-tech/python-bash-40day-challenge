server={
   "Hostname": "web01",
   "os":"Ubuntu",
   "CPU":4
}

print(server["Hostname"])
print(server["os"])
server["RAM"] = "8gb"

print(server)


for key,value in server.items():
   print(key,":",value)
