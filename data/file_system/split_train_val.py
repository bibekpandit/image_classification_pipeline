import os, shutil
import pdb
import random

def splitTraining(src_dir, destination_dir, fraction_for_validation):
    """
    Splits the training data into training set and validation set. Directories
    train and validate must exist inside destination_dir. Training set will be put
    inside train directory of destination_dir and validation set inside valid directory
    of destination_dir.

    Args:
    src_dir : directory containing the unsplitted data
    destination_dir : directory where the splitted trainig and validation sets
                             will be stored
    fraction_for_validation : fraction of original data that should be used for
                                     creating validation set.
    """
    directory = os.fsencode(src_dir)
    for label in os.listdir(directory):
        label_name = os.fsdecode(label)
        label_path = src_dir + "/" + label_name
        print(label_name)
        # iterate over all the lable folders
        for [path, dirname, files] in os.walk(label_path):
            num_of_valid_files = int(len(files) * fraction_for_validation)
            random.shuffle(files)

            # creating validation set
            for file in files[:num_of_valid_files]:
                validate_path = "{0}/validate/{1}".format(destination_dir, label_name)
                if not os.path.exists(validate_path):
                    os.mkdir(validate_path)
                shutil.copy("{0}/{1}".format(path, file), validate_path)

            # creating training set
            for rest in files[num_of_valid_files:]:
                train_path =  "{0}/train/{1}".format(destination, label_name)
                if not os.path.exists(train_path):
                    os.mkdir(train_path)
                shutil.copy("{0}/{1}".format(path, rest), train_path)
