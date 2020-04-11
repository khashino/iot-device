#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import ConfigParser
import io
from suds.client import Client

with open("/project/config.ini") as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

#url = "http://192.168.137.132:7001/soa-infra/services/default/RestServiceDBv1/setclockbpel_client_ep?WSDL"
url = config.get('sync', 'url')
#headers = config.get('sync', 'headers')
clockfile = config.get('other', 'clockfile')
syncfile = config.get('other', 'syncfile')

def soapreq(fid,fname,lname,datetime):
    client = Client(url)
    client.service.process(fid,fname,lname,datetime)

def resync():
    with open(clockfile, "r") as fp:
        for line in fp:
            #print line
            #['1', 'khashayar', 'norouzi', '2020/02/18-12:51:20', '0\n']
            clockdata = line.split(",")
            fid = clockdata[0]
            fname = clockdata[1]
            lname = clockdata[2]
            datetime = clockdata[3]
            soapreq(fid,fname,lname,datetime)
            try:
                fl = open(syncfile, "a")
                clock_data = fid + "," + fname + "," + lname + "," + datetime + ",1\n"
                #print(clock_data)
                fl.write(clock_data)
                fl.close()
            except Exception as e:
                raise
    os.remove(clockfile)
