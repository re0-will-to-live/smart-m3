from random import randint
from datetime import datetime
from smart_m3.m3_kp_api import *
from time import sleep

# python server.py <NUMBER>

class Server:
    def __init__(self, result):
        self.result = int(result)
        self.flag = True

    def handle(self, added, removed):
        # print(f'Guess reporting: {datetime.now()}')
        for data in added:
            # print(data)
            if data[1].value == 'guesses':
                print(f'{data[0]} try {data[2]}')
                if int(data[2].value) != self.result:
                    res = 'No'
                else:
                    res = int(data[2].value)
                print(res)
                insert_list = [
                    Triple(data[0], URI('result'), Literal(res)),
                ]

                self.kp.load_rdf_remove(data)
                self.kp.load_rdf_insert(insert_list)
                self.flag = False

    def run(self):
        self.kp = kp = m3_kp_api(PrintDebug=True)

        subscription_triple = Triple(None, URI('guesses'), None)
        handler = self
        handler_subscription = kp.load_subscribe_RDF(subscription_triple, handler)
        try:
            while True:
                sleep(5)
        except KeyboardInterrupt:
            print('NOOOOOOO')

        kp.load_unsubscribe(handler_subscription)
        kp.clean_sib()  # remove all data from Smart Space
        kp.leave()

import sys

Server(sys.argv[1]).run()
