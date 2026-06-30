class Server:
   def __init__(self, name):
       self.name= name

   def details(self):
       print("Server:", self.name)



class LinuxServer(Server):
   def install_nginx(self):
       print("Installing Nginx on", self.name)



server = LinuxServer("Prod-01")
server.details()
server.install_nginx()
