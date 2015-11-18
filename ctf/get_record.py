# coding=UTF-8

import time
import requests


t = int(time.time())
print requests.get("http://localhost:8080/getrecord.php", params={
    'secret': 'mysecret',
    'begin_time': t,
    "end_time": t + 10
}).text

# expected
result = [
    {
        'ip': '191.2.1.1',
        'flag': 'falgs',
        'time': 199392,
        'id': 192
    }
]
