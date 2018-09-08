import get_data

def get_description(mongo_collection, my_photos):
    """
    Get the description corresponding to the photos in my_photos and put
    the (photo_id , description) pair in a list.

    Args:
    mongo_collection: mongo database collection of where to seach for photos
    my_photos: list of the photo ids
    """

    find_dictionary = {"attributes.photos": {"$in":my_photos}}
    filter_dictionary = {'description':1, 'attributes':1}
    # docs_containing_photos is a cursor object (an iterable that gives documents)
    docs_containing_photos = mongo_collection.find(find_dictionary, filter_dictionary)
    full_set = set()
    set_of_my_photos = set(my_photos) # now checking if a photo exists in initial list
                                      # takes O(1) time insted of O(n) in the line below

    # for every document, for every photo in the document, we check if that photo lies in
    # my_photos and if it does, we add it to the full_set along with the description
    for doc in docs_containing_photos:
        photos_in_current_doc = set(doc['attributes']['photos'])
        current_description = doc['description']
        for photo in photos_in_current_doc:
            if photo in set_of_my_photos:
                full_set.add((photo, current_description)) # we use set to avoid duplicate (photo, description) pair

    return list(full_set)

def getImageAndDescription(mongo_collection, dict_with_only_ids):
    """
    Takes a dictionary mapping labels to photoIDs and returns another dictionary
    where the labels map to photoIDs as well as the description.

    Args:
    dict_with_only_ids: dictionary whose keys are labels (string) and its
                        values are lists of photIDs (string) belonging to that label
    """
    dict_with_des = {} # new dictionary for (photoID, description) pair

    for label in dict_with_only_ids:
        print(label)
        dict_with_des[label] = get_description(mongo_collection, dict_with_only_ids[label])

    return dict_with_des
