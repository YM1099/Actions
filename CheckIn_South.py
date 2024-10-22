import os
import requests

headers_southplus = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
    'Cookie': os.getenv('COOKIE_SOUTH')
}

def request(method, url, headers):
  if method == 'get':
    r = requests.get(url, headers=headers)
  elif method == 'post':
    r = requests.post(url, headers=headers)
  print(r.text)

request('get', 'https://www.south-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job&cid=15&verify=bff8997b', headers_southplus)
request('get', 'https://www.south-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job&cid=14&verify=bff8997b', headers_southplus)
request('get', 'https://www.south-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job2&cid=15&verify=bff8997b', headers_southplus)
request('get', 'https://www.south-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job2&cid=14&verify=bff8997b', headers_southplus)
