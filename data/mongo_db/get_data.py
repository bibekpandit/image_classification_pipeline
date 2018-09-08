import pymongo
from pymongo import MongoClient


def getClient(IP_address):
    """
    Returns the Mongo Client at the IP_address

    Args:
    IP_address : string IP address
    """
    return MongoClient(IP_address)

def getCollection(mongo_client, db_name, collection_name):
    """
    Get collection with collection_name

    Args:
    mongo_client : mongo client to get collection from
    db_name : name of the database collection is contained in
    collection_name : name of the collection
    """
    db = mongo_client[db_name]
    return db[collection_name]

def findInMongoCollection(mongo_collection, find_dictionary, filter_dictionary = None):
    """
    Search the mongo_collection for docs satisfying the criteria in find_dictionary.

    Args:
    mongo_collection : mongo collection to perform find upon
    find_dictionary : dictionary providing search criteria. It may look like
                      {"animal" : "cat", "place": ...}
    filter_dictionary : if you only want certain parts of the document, you
                        put a filter_dictionary. if you only want descriptions, for example,
                        your filter_dictionary will look like {"description" : 1 , "_id":0}
    """
    if filter_dictionary == None:
        return mongo_collection.find(find_dictionary)
    return mongo_collection.find(find_dictionary, filter_dictionary)

def getInfoFromDict(nested_dict, list_of_nested_attributes):
    """
    Get info from nested_dict using the list_of_nested_attributes

    Args:
    nested_dict : dictionary that is json type (dictionary mapping to dictionary])
    list_of_nested_attributes : list of attributes that specifies the information
                                demanded from nested_dict. If you want photIDs that
                                are in attributes, the list is ['attributes', 'photos'].
                                List cannot be empty
    """
    if len(list_of_nested_attributes) == 1:
        return nested_dict[list_of_nested_attributes[0]]
    else:
        return getInfoFromDict(nested_dict[list_of_nested_attributes[0]],
                               list_of_nested_attributes[1:])
