# coding=UTF-8

import requests
import json


requests.post("http://localhost:8080/detect.php", data=json.dumps({
    "name": 'serviceName',
    "hosts": [
        '172.16.12.22',
        "172.16.13.22"
    ]
}))

# expected result
r = [
    {
        'host': '172.16.12.22',
        'available': True,
        'detail': 'all ok'
    },
    {
        'host': '172.16.13.22',
        'available': False,
        'detail': 'post failed'
    }
]
