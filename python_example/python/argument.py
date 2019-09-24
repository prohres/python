import sys
import os

x = len(sys.argv)

if x > 1:
    print("Arguments entered: " + str(sys.argv[1:]))
else:
    print("Arguments NOT entered!")

os.system("date")
sys.exit()

