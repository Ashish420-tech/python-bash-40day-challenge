class Server:
   def __init__(self,name):
       self.name= name

class LinuxServer(Server):

   def __init__(self, name, ip):
       super().__init__(name)
       self.ip = ip

   def show(self):
      print(self.name,self.ip)



obj = LinuxServer("Web01","192.168.1.0")

obj.show()
