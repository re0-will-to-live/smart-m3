from datetime import datetime
from smart_m3.m3_kp_api import *
from time import sleep

class KP_Handler:
    def __init__(self, kp=None):
        self.kp = kp

    def handle(self, added, removed):
        print('Agent_X reporting: {}'.format(datetime.now()))
        print('    added', added)
        print('    removed', removed)

        for data in added:
            print(f'{data} added')
            if int(data[2].value) % 2 == 0:
                kp.load_rdf_remove(data)

        for data in removed:
            print(f'{data} removed')



kp = m3_kp_api(PrintDebug=True)

subscription_triple = Triple(URI('Agent_X'), None, None)
handler = KP_Handler(kp)
handler_subscription = kp.load_subscribe_RDF(subscription_triple, handler)

try:
    sleep(50)
except KeyboardInterrupt:
    pass
kp.load_unsubscribe(handler_subscription)
kp.leave()
exit(0)