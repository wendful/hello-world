import requests

req = requests.get('http://baidu.com/')
print(type(req))
print(req.status_code)
print(req.encoding)
print(req.cookies)