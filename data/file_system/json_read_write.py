import json

def readJsonData(json_file):
    """
    Reads json_file's data and returns it as a Python dictionary

    Args:
    json_file: path of the json file to be read along with .json extension
    """
    with open(json_file) as data:
        return json.load(data)

def writeDictToJson(dict, json_file):
    """
    Saves dictionary dict to filename (creates file with filename if it does not exist already)

    Args:
    dict : dictionary to be saved
    filename : name of the file dict is to be saved to.
    """
    if not json_file.endswith('.json'):
        json_file = json_file + '.json'

    j = json.dumps(dict)
    f = open(json_file,'w')
    f.write(j)
    f.close()
