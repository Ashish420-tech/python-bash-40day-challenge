class Server:

    def __init__(self, name, ip, os):

        self.name = name
        self.ip = ip
        self.os = os

server = Server(
    "WebServer",
    "192.168.1.20",
    "Ubuntu"
)

print(server.name)
print(server.ip)
print(server.os)
