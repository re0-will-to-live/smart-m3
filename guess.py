from random import randint
from datetime import datetime
from smart_m3.m3_kp_api import *
from time import sleep

# python guess.py <AGENT_NAME>

class Guesser:
    def __init__(self, name, limits=(0, 100)):
        self.guesses = list(range(*limits))
        self.name = name
        self.flag = True

    def guess(self):
        index = randint(0, len(self.guesses))
        try:
            val = self.guesses.pop(index)
        except:
            return
        print(f'try {val}')
        insert_list = [
            Triple(URI(self.name), URI('guesses'), Literal(val)),
        ]

        self.kp.load_rdf_insert(insert_list)

    def handle(self, added, removed):
        # print(f'{self.name} reporting: {datetime.now()}')
        for data in added:
            # print(data)
            if data[1].value == 'result':
                if data[2].value != 'No':
                    print(f'yeeee {data[2]}')
                    self.flag = False
                self.kp.load_rdf_remove(data)

    def run(self):
        self.kp = kp = m3_kp_api(PrintDebug=True)

        subscription_triple = Triple(URI(self.name), URI('result'), None)
        handler = self
        handler_subscription = kp.load_subscribe_RDF(subscription_triple, handler)
        try:
            while len(self.guesses) and self.flag:
                self.guess()
                sleep(1)
        except KeyboardInterrupt:
            print('NOOOOOOO')

        kp.load_unsubscribe(handler_subscription)
        kp.leave()

import sys

Guesser(sys.argv[1]).run()
