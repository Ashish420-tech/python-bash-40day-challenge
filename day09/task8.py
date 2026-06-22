class EC2:


   def __init__(self,name,state):
       self.name=name
       self.state=state

   def status(self):
       print(f"{self.name} ->{self.state}")


server1=EC2("Webserever","Running")
server2=EC2("DBServer","Stopped")


server1.status()

server2.status()
