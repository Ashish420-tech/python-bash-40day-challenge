#!/bin/bash

read -p "Enter path:" path

if [ -e "$path" ]
then
   echo "Exists"
  
   if [ -f "$path" ]
   then 
     echo "Regular File"
   fi

   if [ -d "$path" ]
   then
     echo "Directory"
   fi
   
   if [ -r "$path" ]
   then
     echo "Readable"
   fi
   
   if [ -w "$path" ]
   then
      echo " Writable"
   fi
   
   if [ -x "$path" ]
   then
     echo "Executable"
   fi

   if [ -s "$path" ]
   then
     echo "Not empty"
   fi
   
   if [ -L "$path" ]
   then
     echo "Symbolic Link"
   fi

else
   echo " Path doesnot exist"
fi
