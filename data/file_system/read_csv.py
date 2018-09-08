import csv
import os
import re
import json
import json_read_write

def readIDs_in_csv(csv_file_path):
    """
    Reads a csv file and returns a set of photo ids contained
    in the formulas in the csv file.

    Args:
    csv_file_path : (string) path of the csv file. The columns of the
                    csv file are "photoID" and "URL to the photo"
    """
    set_of_ids_in_csv = set()

    with open(csv_file_path, newline = "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")

        for row in csvreader:
            set_of_ids_in_csv.add(row[0])

        return set_of_ids_in_csv

def getAllIDs(directory_path_of_csv_files):
    """
    Returns all the photo ids from csv files in a directory
    as a set.

    Args:
    directory_path_of_csv_files : (string) path of directory containing csv files
    """
    directory = os.fsencode(directory_path_of_csv_files)
    big_set = set()
    for csv_file in os.listdir(directory):
        csv_filename = os.fsdecode(csv_file)
        file_path = directory_path_of_csv_files + "/" + csv_filename
        big_set.update(existingIDs(file_path))
    return big_set

def getIDBylabel(directory_path_of_csv_files):
    """
    Returns a dictionary mapping csv file names to the photo ids contained in the
    corresponding csv files.

    Args:
    directory_path_of_csv_files : (string) path of directory containing csv files
    """
    directory = os.fsencode(directory_path_of_csv_files)
    whole_dict = {}
    for csv_file in os.listdir(directory):

        csv_filename = os.fsdecode(csv_file)
        file_path = directory_path_of_csv_files + "/" + csv_filename

        label = re.sub("\.csv$", "", csv_filename)
        whole_dict[label] = list(readIDs_in_csv(file_path))

    return whole_dict


# Write $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def getPhotoForCsv(photoId):
    """
    Get photoId and convert into a formula that the spreadsheet can
    take and convert into image.
    """
    ROOT = "https://mywebsite.com/image-collection/" # not currently an actual webpage
    link_to_photo = ROOT + photoId
    return '=IMAGE("%s", 1)' % link_to_photo

def writeToCSV(dict_with_des, destination_dir):
    """
    Write the contents of d into csv files. For each label
    in d, a new csv file is created.

    Args:
    dict_with_des: dictionary mapping label to a list of (photoId, description)
                   tuples. The csv file for a one label contains rows of photo formula
                   (parsable in google sheets) and description associated with the photo
    destination_dir: path to folder where the CSVs will be stored
    """

    for label in dict_with_des:
        csv_filename = "{0}/{1}.csv".format(destination_dir, label)
        with open(csv_filename, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter='|')

            for photoId, description in d[label]:
                photo_for_csv = getPhotoForCsv(photoId)
                filewriter.writerow([photo_for_csv, description])

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

possible_labels = {'cat', 'dog', 'mouse', 'rabbit'}

def csv_to_labeled_data(csv_file_path, possible_labels = possible_labels):
    """
    Reads a csv file and returns a dictionary of labels as keys mapping to photo ids as values.
    This method differs from earlier ones in that one csv file contains all the
    images with its different labels. The labels have a separate column

    Args:
    csv_file_path : (string) path of the csv file. column1 : Image Id
                    column2: image formula, column3 and beyond: multiple labels
    """
    dict_of_photoIDs = {}
    with open(csv_file_path, newline = "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")

        for row in csvreader:
            ID = row[0]

            for label in row[2:]:
                label = label.strip()
                if label == '':
                    break
                assert label in possible_labels
                if label in dict_of_photoIDs:
                    dict_of_photoIDs[label].append(ID)
                else:
                    dict_of_photoIDs[label] = [ID]

        return dict_of_photoIDs
