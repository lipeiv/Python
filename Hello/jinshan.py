import requests

res = requests.get("http://fy.iciba.com", params = {'key':'value'})

print(res)