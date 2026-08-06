#!/bin/bash

echo "dev1:Password@123" | chpasswd
echo "dev2:Password@123" | chpasswd
echo "qa1:Password@123" | chpasswd
echo "devops1:Password@123" | chpasswd
echo "manager1:Password@123" | chpasswd

echo "Passwords Configured."
