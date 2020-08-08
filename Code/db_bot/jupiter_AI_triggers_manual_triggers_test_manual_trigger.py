

def get_trigger(fromDate,toDate,pos,origin,destination,compartment):  

    import requests
    import json
    
    url = "http://******"
    
    
    fromDate= fromDate
    toDate = toDate
    pos = pos
    origin = origin
    destination = destination
    compartment = compartment
    
    parameters = [{
        "fromDate": fromDate,
        "toDate": toDate,
        "pos": pos,
        "origin": origin,
        "destination": destination,
        "compartment": compartment,
        "reason": "R1",
        "work_package_name": "WP1",
        "flag": "M"
    }]
    # '''
    
    headers = {"Connection": "keep-alive",
               "Content-Length": "33354",
               "Host" : "13.235.125.244:5000",
               "X-Requested-With": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
               "Content-Type": "application/json",
               "Accept": "*/*",
               "Accept-Encoding": "gzip,deflate",
               "Accept-Language": "q=0.8,en-US",
               "Accept-Charset": "utf-8"
               }
    
    
    response = requests.post(url, data=json.dumps(parameters), headers=headers)
    od = origin+destination
    
    from pymongo import MongoClient
    client = MongoClient('****')
    fzdb = client['****']
    myCollection = fzdb['*****']
    
    answer = list(myCollection.find({
            "dep_date_start" : fromDate,
            "dep_date_end" : toDate,
            "pos" : pos,
            "od" : od,
            "compartment" : compartment
            }))
    
    return answer


