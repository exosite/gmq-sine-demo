#!/usr/bin/env python

# pylint: disable=W0312

import requests, time, sys
from urllib import urlencode
from math import *

def main(product_id, serial, USING_GMQ):

    print("Starting with product.id: {}, serial: {}, USING_GMQ: {}"
        .format(product_id, serial, USING_GMQ)
    )

    if not USING_GMQ:

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

            cik = r.text
            if 40 != len(cik):
                print("Got bad cik '{}' from Murano, exiting.".format(cik))
                sys.exit(-1)
            print("Got good cik from Murano: {}".format(cik))

            with open('gmq_demo.cik','w') as cikfile:
                cikfile.write(cik)

    while True:
        test_data = int(100 * cos(radians(time.clock()) * 100))
        print("Writing {} to {}.".format(test_data, "GMQ" if USING_GMQ else "Murano"))

        url = "http{}://{}{}/onep:v1/stack/alias".format(
            ''                  if USING_GMQ else 's',
            ''                  if USING_GMQ else product_id+'.',
            'localhost:8090'    if USING_GMQ else 'm2.exosite.com'
        )

        headers = {'X-Exosite-CIK': '{}'.format(cik)}

        data = { 'sine-data': test_data }

        print("url: {}".format(url))
        print("headers: {}".format(headers))
        print("data: {}".format(data))

        r = requests.post(url,headers=headers,data=data)
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

