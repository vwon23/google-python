import urllib.request
import urllib.parse

#x = urllib.request.urlopen(url)
#print(x.read())

url = 'http://www.google.com'
values = { 'gws_rd' : 'ssl',
           'q' : 'wtf' }
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)           
           