from smart_m3.m3_kp_api import *
import random
from time import sleep

if __name__ == '__main__':
    # basic program, which connects to the smart space and clears it
    kp = m3_kp_api(PrintDebug=True)

    insert_list = [
        Triple(URI('Agent_X'), URI('has_temperature'), Literal(10)),
        Triple(URI('Agent_X'), URI('wind_direction'), Literal('SW')),
        Triple(URI('Agent_X'), URI('send_data'), URI('Agent_Y')),
    ]

    kp.load_rdf_insert(insert_list)

    kp.load_query_rdf(Triple(URI('Agent_X'), URI('send_data'), URI('Agent_Y')))
    print('Query result about Agent_X send_data Agent_Y in the smart space: {}\n----------------------------'.format(kp.result_rdf_query))
    kp.load_query_rdf(Triple(URI('Agent_X'), None, None))
    print('Query result about Agent_X in the smart space: {}'.format(kp.result_rdf_query))

    kp.load_query_rdf(Triple(None, URI('has_temperature'), None))
    new = [Triple(triple[0], triple[1], Literal(random.randint(-10, 20))) for triple in kp.result_rdf_query]
    kp.load_rdf_update(new, kp.result_rdf_query)

    kp.load_rdf_remove(Triple(URI('Agent_X'), URI('send_data'), None))
    try:
        for _ in range(10):
            sleep(5)
            insert_list = [
                Triple(URI('Agent_X'), URI('has_item'), Literal(random.randint(0, 20))),
            ]
            kp.load_rdf_insert(insert_list)
            kp.load_query_rdf(Triple(URI('Agent_X'), URI('has_item'), None))
            print('Query result about URI(Agent_X), URI(has_item) in the smart space: {}'.format(kp.result_rdf_query))
    except KeyboardInterrupt:
        pass
    kp.clean_sib()  # remove all data from Smart Space
    kp.leave()
