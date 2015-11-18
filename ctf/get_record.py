# coding=UTF-8

import time
import requests


t = int(time.time())
print requests.get("http://localhost:8080/records.php", params={
    'begin_time': t,
    "end_time": t + 10
}).text
