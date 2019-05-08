import requests

r = requests.get("http://coreyms.com'")
print(r.status_code)
print(r.ok)
