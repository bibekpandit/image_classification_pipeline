import pymongo
from pymongo import MongoClient
import sys, os

import get_data

def getIdFromCursor(cursor_of_documents, get_description):
    """
    Returns the list of photo IDs (with or without description) contained in each document in the cursor_of_documents.

    Args:
    cursor_of_documents : a cursor object which is an iterable instance of documents
    get_description : boolean value specifying whether to get descriptions along with photoIDs
    """

    list_of_ids = []
    for doc in cursor_of_documents:
        list_of_photoIDs = get_data.getInfoFromDict(doc, ['attributes', 'photos'])
        if get_description:
            description = get_data.getInfoFromDict(doc, ['description'])
            photo_with_description = [[photo, description] for photo in list_of_photoIDs]
            list_of_ids.extend(photo_with_description)
        else:
            list_of_ids.extend(list_of_photoIDs)
    return list_of_ids


def getPhotoIdFromCollection(collection, labelID, get_description):
    """
    Retuns the list of photo IDs (with or without description) that are present in the collection which tags to labelID.

    Args:
    collection : collection to be searched on
    labelID : ID of the label contained in facet
    get_description : boolean value specifying whether to get descriptions along with photoIDs
    """

    find_dictionary = {"facets":labelID}
    cursor_of_found_docs = get_data.findInMongoCollection(collection, find_dictionary)
    return getIdFromCursor(cursor_of_found_docs, get_description)


def getPhotosForAlllabels(mongo_collection, dict_of_labelIDs, get_description = False):
    """
    Returns a dictionary mapping label (name) to the photo IDs (with or without description)

    Args:
    mongo_collection : collection to be search upon for photoIDs
    dict_of_labelIDs : a dictionary that maps label ID's to label names.
    get_description : boolean value specifying whether to get descriptions along with photoIDs,
                      set to False by default
    """

    map_labelID_to_photoID = {}

    for labelID in dict_of_labelIDs:
        label_name = dict_of_labelIDs[labelID]
        print(label_name)
        map_labelID_to_photoID[label_name] = getPhotoIdFromCollection(mongo_collection, labelID, get_description)

    return map_labelID_to_photoID
