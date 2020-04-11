#!python
from suds.client import Client

url = 'http://192.168.137.132:7001/soa-infra/services/default/RestServiceDBv1/setclockbpel_client_ep?WSDL'
client = Client(url)
print client
client.service.process("av","av","av","av")
