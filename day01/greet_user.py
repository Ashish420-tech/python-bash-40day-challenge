import sys

if len(sys.argv) < 2:
   print("Usage: python3 greet_user.py <name>")
else:
   print("Hello ", sys.argv[1])
