servers = [

  {"name":"Web","status":"Running"},
  {"name":"DB","status":"Stopped"},
  {"name":"Cache","status":"Running"}

]

for server in servers:
   print(server["name"], server["status"])
