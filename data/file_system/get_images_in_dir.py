import os
import re
from PIL import Image

# Part 1: Get all the photoIDs contained in a directory and its sub-directories
# and put them in a set

def isImage(file_path):
    '''
    Returns if file with file_path is an image type. This method might not work for
    uncommon image files like xcf but works for almost all common image formats.

    Args:
    file_path: string path to file
    '''
    most_common_img_extensions = ['.tif', '.tiff', '.gif', '.jpeg', '.jpg', '.jif', '.jfif',
                                  '.jp2', '.jpx', '.j2k', '.j2c', '.fpx', '.pcd', '.png']

    extension = os.path.splitext(file_path)[1]
    if extension in most_common_img_extensions:
        return True
    else:
        try:
            Image.open(file_path)
            return True
        except IOError:
            return False


def storeAllPhotoInSet(directory_path, set_of_ids):
    """
    It is more of a helper function to getPhotosInDir.
    Stores the names of images contained in directory and its sub-directories in the given set.

    Args:
    directory_path: path to directory for which photo names are requested
    set_of_ids: set where the photo names (during original usage ids) are stored
    """

    directory = os.fsencode(directory_path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        path_to_file = "{0}/{1}".format(directory_path, filename)

        # if we find a directory inside the directory, recursively check
        # for photos in that directory
        if os.path.isdir(path_to_file):
            storeAllPhotoInSet(path_to_file, set_of_ids)

        elif isImage(path_to_file):
            photoId = os.path.splitext(filename)[0] # strip out the extension
            set_of_ids.add(photoId)

def getAllPhotosInDir(directory_path):
    """
    Returns a set containing the names of all the photos
    in the directory.

    @param directory_path: path to directory for which photo names are requested
    """
    set_of_all_ids = set()
    storeAllPhotoInSet(directory_path, set_of_all_ids)
    return set_of_all_ids


# Part 2: Store the photoIDs in the in a dictionary as values whose key is the
# label the photoIDs belong to
def photosBylabel(src_directory_path):
    """
    Returns a dictionary whose keys are the sub directories in src_directory. (In our
    case that represents the label) And the values are the files in the corresponding
    directory.

    @param src_directory_path : path to the source directory
    """
    dict_of_photoIDs = {} # new dictionary that will be returned
    directory = os.fsencode(src_directory_path)

    for sub_dir in os.listdir(directory):
        sub_dir_name = os.fsdecode(sub_dir)

        path_to_sub_dir = "{0}/{1}".format(src_directory_path, sub_dir_name)
        if os.path.isdir(path_to_sub_dir):

            photo_id_list = list(getAllPhotosInDir(path_to_sub_dir))
            dict_of_photoIDs[sub_dir_name] = photo_id_list

    return dict_of_photoIDs
