class Monitoring:

   def monitor(self):
       print("Monitoring Enabled")


class Backup:

   def backup(self):
      print("Backup Started")


class Server(Monitoring, Backup):
   pass


s= Server()
s.monitor()
s.backup()
