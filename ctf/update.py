# coding=UTF-8

import requests
import json


print requests.post("http://localhost:8080/getflag.php", data=json.dumps([
    {
        "ip": '192.168.16.2',
        "flag": "1asfjaslkdfja;ksldjfk"
    },
    {
        "ip": '192.168.17.2',
        "flag": "aksdlfjaknvaksldfksajl"
    }
])).text