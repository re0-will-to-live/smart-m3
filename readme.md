# Project skeleton for Smart Space application

## How to install

0. _Use the virtualenv, Luke!_ (c) 
1. `pip install -r requitements.txt`



## Smart-M3 operations

`from smart_m3.m3_kp_api import *` - import all package data

### Triplets

`` Subject, Predicate, Object ``
`` Triple(URI(...), URI(...), URI(...)/Literal(...)) ``

```
Triple(
URI("http://www.ducatienergia.com/SIIP2P.owl#SensorData_829889475"), 
URI("http://www.ducatienergia.com/SIIP2P.owl#HasSensorDataValue"), 
Literal(10))

Triple(
URI("http://www.ducatienergia.com/SIIP2P.owl#SensorData_829889475"), 
URI("http://www.ducatienergia.com/SIIP2P.owl#HasSensorDataValue"), 
None) # only for query/subscription !!!
```

### Join

``kp = m3_kp_api(... options here ...)``

### Leave

`` kp.leave() ``


### Insert

```
kp.load_rdf_insert(Triple | List[Triple])
```

### Remove

```
kp.load_rdf_remove(Triple | List[Triple])

### Also it is possible to use NONE (wildcard) for ingnoring some on the triplet parts
### Triple(URI('test'), None, None) will remove all triplets, where subject == URI('test')
```

### Query

```
### rdf-triples
kp.load_query_rdf(Triple(...)) # may contain wildcards !
for result in kp.result_rdf_query:
    print(result)
    
### sparql
kp.load_query_sparql('....')
    for res in kp_test.result_sparql_query:
	    for result in res:
	        print(result)
```


### Subscribe / Unsubscribe

At first, you need to declare your handler class

```
class KP_Handler():
    def __init__(self, kp=None)
        self.kp = kp
    
    def handle(self, added, removed):
        """"
            added - list of information which was added
            removed - list of information which was removed
        """"
        
        for result in added:
            print(added)
            
        for result in removed:
            print(removed)
```

After that, you can create your subscription (e.g. which will listen all data):

```
    handler = KP_Handler(kp)
    rdf_subs_triple = Triple(None, None, None) # will listen ALL data
    rdf_subscription = kp.load_subscribe_RDF(rdf_subs_triple, handler) # handler will work in separate thread
    
    
    ### some inserting, pausing, and so on ###
    
    
    # leave smart space
    kp.load_unsubscribe(rdf_subscription)
    kp.leave()
```
