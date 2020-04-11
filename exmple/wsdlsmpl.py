import requests
url = 'http://192.168.137.132:7001/soa-infra/services/default/RestServiceDBv1/setclockbpel_client_ep?WSDL'
lname = "khashayar"
fname = "norouzi"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<?xml version = '1.0' encoding = 'UTF-8'?>
<env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://www.example.org">
   <env:Header/>
   <env:Body>
      <ns1:input>
         <ns1:fid>123</ns1:fid>
         <ns1:fname>"""+fname+"""</ns1:fname>
         <ns1:lname>"""+lname+"""</ns1:lname>
         <ns1:datetime>123</ns1:datetime>
      </ns1:input>
   </env:Body>
</env:Envelope>
"""

response = requests.post(url,data=body,headers=headers)
print response.content
