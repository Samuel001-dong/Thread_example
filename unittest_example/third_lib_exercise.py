""""

"""
import requests
r = requests.get("http://www.baidu.com")
p = requests.post("http://httpbin.org/post", data={'key': 'value'})
print(p.text)
print(r.status_code)
print(r)
r.encoding = "utf-8"
print(r.text)
