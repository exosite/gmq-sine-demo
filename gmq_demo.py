#!/usr/bin/env python

# pylint: disable=W0312

import requests, time
from math import *

def main():

    while True:
        data = int(100 * cos(radians(time.clock()) * 100))
        print("Writing {} to gmq.".format(data))

        r = requests.post(
            "http://localhost:8090/onep:v1/stack/alias",
            headers={'X-Exosite-VMS': 'dubhxzv0r4e1m7vi dubhxzv0r4e1m7vi 12345'},
            data={'test':data}
        )
        print(r)
        time.sleep(5)

if __name__ == '__main__':
    main()

