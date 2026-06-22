class Linux:

   def version(self):
      print("Ubuntu")


class Server(Linux):
  

   def version(self):
      print("Ubuntu 24.04")


obj = Server()
obj.version()
