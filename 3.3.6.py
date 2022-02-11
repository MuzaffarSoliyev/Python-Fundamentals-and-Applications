import requests
import re

url1 = input()
url2 = input()

proxyDict = {
    "https": "http://10.9.0.29:42897",
    "http": "http://10.9.0.29:42897"
}

res_1 = requests.get(url1, proxies=proxyDict)

found = False
links = re.findall(r'<a.+</a>', res_1.text)

for link in links:
    l = re.findall(r'".+"', link)
    res_i = requests.get(l[0][1: len(l[0]) - 1], proxies=proxyDict)
    links_i = re.findall(r'<a.+</a>', res_i.text)
    for sublink in links_i:
        links_i = re.findall(r'".+"', sublink)
        if url2 == links_i[0][1: len(links_i[0]) - 1]:
            found = True
            print('Yes')
            break
    if found:
        break

if not found:
    print('No')
