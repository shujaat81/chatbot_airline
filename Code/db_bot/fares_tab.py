
# Function to get lowest fare for different carriers

def lowest_fare(origin,destination,compartment,dep_date_start,dep_date_end):
    from pymongo import MongoClient
    client = MongoClient('*****')
    db = client['****']
    collection = db['****']
    

    
    result = list(collection.aggregate([
         {
             '$match':
                 {
                     'origin': origin,
                     'destination': destination,
                     'compartment':compartment,
                     "$or": [
                              {"effective_from" :{"$lte":dep_date_start}},
                              {"effective_from" : {"$eq": None}}
                     ],
                     "$or": [
                         {"effective_to":{"$gte":dep_date_end}},
                         {"effective_to":{"$eq":None}}
                     ]
                 }
         },
         {
             '$group':
                 {
                     '_id': {
                         'carrier': "$carrier",
                         'origin': '$origin',
                         'destination': '$destination',
                         'compartment': '$compartment'
                     },
                     'total_fare': {'$min': '$total_fare'}
                 }
         },
         {
             '$project': {
                 'total_fare': 1,
                 'carrier': '$_id.carrier',
                 'origin': '$_id.origin',
                 'destination': '$_id.destination',
                 'compartment': '$_id.compartment',
                 '_id': 0
             }}
     ]))

    return result

# Function for filling fare to ATPCO by calling java API
def ATPCO_auto_filing(total_fare,carrier,origin,destination,compartement):
    
    '''
    Input parameters: total_fare, carrier, origin, destination, compartement
    Return : _id,fare_basis,oneway_return,origin,RBD,destination,compartement,currency,tariff_code,total_fare
    '''
    
    from pymongo import MongoClient
    client = MongoClient('*****')
    db = client['***']
    collection = db['*****']
    
    result = list(collection.find({'total_fare': total_fare, 'carrier': carrier,
                                                                    'origin':origin, 'destination':destination,
                                                                    'compartment':compartement},
                                  {'origin':1,'destination':1,'total_fare':1,'currency':1,
                                   'tariff_code':1,'fare_basis':1,'compartment':1, 'oneway_return':1,'RBD':1}))

    
    return result[0]


def currency(currency_from,currency_to):
    from pymongo import MongoClient
    client = MongoClient()








