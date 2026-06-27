class Server:

    def __init__(self,name):
        self.name = name

    def start(self):
        print(self.name,"Started")

    def stop(self):
        print(self.name,"Stopped")


server=Server("Database")

server.start()
server.stop()
