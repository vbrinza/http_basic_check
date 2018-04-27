#!/usr/bin/env python

import requests
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-u', help='Host to be checked')
args = parser.parse_args()
2xx = ['200', '201', '202']
4xx = ['400', '401', '402']
5xx = ['500', '501', '502']

r = requests.get(args.u)
if r.status_code in 2xx:
    print("OK")
    sys.exit(0)
elif r.status_code in 4xx:
    print("WARNING")
    sys.exit(1)
elif r.status_code in 5xx:
    print("CRITICAL")
    sys.exit(2)
else:
    print("UNKNOWN")
    sys.exit(3)
