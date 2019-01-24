#!/usr/bin/env python3

import os #Imports the os module
import time #Imports the time module

def clear():
  responce = os.system("clear") #Clears the CLI (Command Line Interface)
  
def ref
  responce = os.system("ipconfig /release") #Releases the current Dynamic DHCP IP
  time.sleep(0.5) #Sleeps for 0.5 seconds
  responce = os.system("ipconfig /renew") #Renews a new IP through a IP list connected with your ISP
  time.sleep(0.5) #Sleeps for 0.5 seconds
 
clear() #Calls the 'clear' function
ref() #Calls the 'ref' function
responce = os.system("./DHCPRefresh.py") #Re-opens the program again

# Written By CrimsonTorso
