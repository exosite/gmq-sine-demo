#!/usr/bin/env python

# pylint: disable=W0312

import requests, time, sys
from urllib import urlencode
from math import *

def main(product_id, serial, USING_GMQ):

    try:
        cik = open('gmq_demo.cik', 'r').read()
    except IOError:
        cik = ''


    if 40 != len(cik):
        stuff = urlencode({'vendor':product_id, 'model':product_id, 'sn':serial})
        r = requests.post(
            'https://m2.exosite.com/provision/activate',
            headers={
                'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 
                'Content-Length': len(stuff)
            },
            data=stuff
        )

        print(r.text)
        with open('gmq_demo.cik','w') as cikfile:
            cikfile.write(r.text)

    # sys.exit(1)

    while True:
        data = int(100 * cos(radians(time.clock()) * 100))
        print("Writing {} to gmq.".format(data))

        r = requests.post(
            "https://{}.m2.exosite.com/onep:v1/stack/alias".format(product_id),
            headers= {'X-Exosite-VMS': '{} {} {}'.format(product_id, product_id, serial)} if USING_GMQ else {'X-Exosite-CIK': '{}'.format(cik)},
            data={'test':data}
        )
        print(r)
        time.sleep(5)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: {} <PRODUCT_ID> <SERIAL>".format(sys.argv[0]))
        sys.exit(-1)

    USING_GMQ = False
    if len(sys.argv) == 4:
        USING_GMQ = True if sys.argv[3] == "USING_GMQ" else False

    main(sys.argv[1], sys.argv[2], USING_GMQ)
