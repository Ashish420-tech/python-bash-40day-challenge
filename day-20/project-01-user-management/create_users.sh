#!/bin/bash

echo "Creating User & groups.."

groups=("developers" "qa" "devops" "managers")

for group in "${groups[@]}"
do
   if getent group "$group" > /dev/null
   then
      echo "$group already exist"
   else
      groupadd "$group"
      echo "$group  created"
   fi
done

echo " "

echo "Creating users...."

users=("dev1" "dev2" "qa1" "devops1" "manager1")

for user in "${user[@]}"
do
  if id "$user" &>/dev/nulll
  then
      echo "$user already exists"
  else
      user add -m -s /bin/bash "$user"
      echo "$user created"
  fi
done

echo ""

echo "Assigning groups"

usermod -aG developers dev1
usermod -aG developers dev2
usermod -aG qa qa1
usermod -aG devops devops1
usermod -aG managers manager1

echo ""

echo "Completed Successfully."
