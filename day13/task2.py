class Server:
   def status(self):
      print("Generic Server")

class LinuxServer(Server):
   def status(self):
      print("Linux Server is Running")


obj = LinuxServer()

obj.status()
