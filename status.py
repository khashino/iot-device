import sys, os
from datetime import datetime
import time
import socket
from subprocess import check_output
import ConfigParser
import io

with open("/project/config.ini") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

sleeptime = int(config.get('status', 'sleeptime'))
REMOTE_SERVER = config.get('status', 'remote_server')
#cmd = ["""hostname -I"""]
cmd = ["""hostname -I | awk '{print $1}'"""]
statusfile = config.get('status', 'statusfile')
#cmd = ["""ip route get 1.2.3.4 | awk '{print $7}'"""]
###########################################
def getmyip():
	return check_output(cmd,shell=True)


def net_status(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    s.close()
    return "on"
  except:
     pass
  return "off"


def checker():
	f = open(statusfile, "w")
	status = str(net_status(REMOTE_SERVER))+","+getmyip()
	print(status)
	f.write(status)
	f.close()
	#time.sleep(sleeptime)
