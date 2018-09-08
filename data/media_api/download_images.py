import urllib.request
import os

def getImages(dict, destination_dir_path):
    """
    Download the images whose image URLs are in dict
    and put the photo in the directory corresponding to the key
    it belongs to.

    @param dict : dictionary of keys (labels) mapping to list of string URLs.
                  If the key is "Cat", the list this key maps to must contain
                  URLs of images of cats.
    @param destination_dir_path : path of the directory you want to store the
                                  sub-directories and the images.
    """
    if(not os.path.isdir(destination_dir_path)):
        os.mkdir(destination_dir_path)

    for label in dict:
        current_folder = destination_dir_path + '/' + label
        if(not os.path.isdir(current_folder)):
            os.mkdir(current_folder)

        for i, photo_url in enumerate(dict[label]):
            file_with_path = current_folder + '/' + i + ".jpg"
            try:
                getImage(photo_url, file_with_path)
            except:
                continue

def getImage(url, destination_path):
    urllib.request.urlretrieve(url, destination_path)
