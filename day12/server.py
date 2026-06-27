class Server:

    def __init__(self, name):
        self.name = name


server1 = Server("Web Server")
server2 = Server("Database Server")

print(server1)
print(server2)

print(server1.name)
print(server2.name)
