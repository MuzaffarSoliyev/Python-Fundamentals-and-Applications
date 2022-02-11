import requests
import re

proxyDict = {
    "https": "http://10.9.0.29:42897",
    "http": "http://10.9.0.29:42897"
}

url_to_html = input().strip()

response = requests.get(url_to_html, proxies=proxyDict)
link_pattern = re.findall(r'<a[^>]*?href="(.*?)"[^>]*?>', response.text)

for link in link_pattern:
    pass
