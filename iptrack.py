#!/usr/bin/env python
import os
import time
import requests
import re
ip = input("Hedef ip:")
a = ("http://ip-api.com/json/"+ip)
r = requests.get(a)
print(r.text)
    
