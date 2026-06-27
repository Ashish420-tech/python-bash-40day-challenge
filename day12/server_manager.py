class Server:

    def __init__(self,name,ip,status):

        self.name=name
        self.ip=ip
        self.status=status

    def start(self):
        self.status="Running"

    def stop(self):
        self.status="Stopped"

    def info(self):
        print("Name :",self.name)
        print("IP   :",self.ip)
        print("Status :",self.status)


server=Server(
    "Production",
    "10.0.0.1",
    "Stopped"
)

server.info()

server.start()

server.info()
