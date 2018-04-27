#!/usr/bin/env python

import requests
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-u', help='Host to be checked')
args = parser.parse_args()

r = requests.get(args.u)
if r.status_code == 200:
    print("OK")
    sys.exit(0)
elif r.status_code == 404:
    print("WARNING")
    sys.exit(1)
elif r.status_code == 500:
    print("CRITICAL")
    sys.exit(2)
else:
    print("UNKNOWN")
    sys.exit(3)
