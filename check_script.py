#!/usr/bin/env python

import requests
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-u', help='Host to be checked')
args = parser.parse_args()
two_hundread = [200, 201, 202]
four_hundread = [400, 401, 402]
five_hundread = [500, 501, 502]

r = requests.get(args.u)
if r.status_code in two_hundread:
    print("OK")
    sys.exit(0)
elif r.status_code in four_hundread:
    print("WARNING")
    sys.exit(1)
elif r.status_code in five_hundread:
    print("CRITICAL")
    sys.exit(2)
else:
    print("UNKNOWN")
    sys.exit(3)
