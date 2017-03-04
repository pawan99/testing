from settings import PLAY_HOST
import json
import requests
import time

def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

def process_changed_inventory(product_keys):
    """
            Process products which had clicks/sales to update search_analytics ES
    """
    product_keys = list(set(product_keys))
    url = PLAY_HOST['HOST']+'/productUpdateNotification'
    headers = {'content-type': "application/json"}
    for product_keys_chunk in chunks(product_keys, 1000):
        payload = {'productId': [str(key)
                                 for key in product_keys_chunk], "apiVersionCode": "2"}
        payload = json.dumps(payload)
        res = requests.request("POST", url, headers=headers, data=payload)
        print "udpated ES with product_keys response, ", res.text
        time.sleep(30)
    print "done process_changed_inventory"

