# coding=UTF-8

import requests
import json

requests.post("http://localhost:8080/detect.php", data=json.dumps({
    "request_id": "1asdkfl234",
    "name": 'serviceName',
    "hosts": [
        '172.16.12.22',
        "172.16.13.22"
    ]
}))

requests.get('http://localhost:8080/query.php', params={
    'request_id': 'lasdkfl234'
})

# expected result
r = {
    'request_id': 'lasdkfl234',
    'begin_time': 18188181,
    'end_time': 181819,
    'result': [
        {
            'host': '172.16.12.22',
            'available': True,
            'detail': 'all ok',
            'begin_time': 12412312,
            'end_time': 1239141
        },
        {
            'host': '172.16.13.22',
            'available': False,
            'detail': 'post failed',
            'begin_time': 12412312,
            'end_time': 1239141
        }
    ]
}
