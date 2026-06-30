import os

class FileManager:


   def write_file(self, filename, content):
       with open(filename, "w") as f:
            f.write(content)


   def read_file(self, filename):
       with open(filename) as f:
            print(f.read())

   def append_file(self, filename, content):
       with open(filename, "a") as f:
            f.write(content)


   def delete_file(self, filename):
       if os.path.exists(filename):
            os.remove(filename)
