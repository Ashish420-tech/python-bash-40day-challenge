import os
import shutil

os.makedirs("backup",exist_ok=True)

for file in os.listdir("."):
   if file.endswith(".sh"):
      shutil.copy(file,"backup")
      print(file, "copied")


print("backup Completed")
