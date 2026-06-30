#!/bin/bash

while true
do
echo "1.List Files"
echo "2.Show Date"
echo "3.Exit"

read choice

case $choice in

1) ls ;;
2) date ;;
3) exit ;;
*) echo "Invalid"

esac

done
