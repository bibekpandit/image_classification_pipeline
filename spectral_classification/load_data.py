from PIL import Image
import numpy as np
import os

from spectral_clustering import *

def load_image(infilename):
    """
    Takes the path of an image file and returns a
    numpy array of dimension (1, num_of_pixels) that stores the stores
    the image's pixel values

    @param infilename: path of the image filename
    """
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    data = data.reshape(1, -1) # flatten the numpy array
    return data


def images_to_numpy(directory_path):
    """
    Takes a directory path containing images files and converts
    all them into a single numpy array where each row represents
    an image and each each column represents one of the pixels.

    @param directory_path: string path to the directory containing
                           images
     """
    directory = os.fsencode(directory_path)

    image_paths = [] # stores the path to all images
    data = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith(".jpg"):
            print(filename)
            file_with_path = directory_path + filename
            image_paths.append(file_with_path)
            data.append(load_image(file_with_path))

    return image_paths, np.concatenate(data, axis = 0) # list of numpy array to numpy array


def makeCluster(labels, image_paths):
    """
    After finding the clusters where different images belong,
    makeCluster moves the images into respective directories
    representing respective clusters.

    @param labels: a numpy row vector where an element at index represents
                   the clustere label of the image represented at index
    @param image_paths: list of paths of images that were clustered
    """

    labels_as_list = labels.tolist()
    for i in range(len(labels_as_list)):
        os.rename(image_paths[i], "/Users/bpandit/Documents/GitHub/clusters_new/c%(cnumber)d/img%(inum)d.jpg"
                                  % {'cnumber':labels[i], 'inum':i})






# if __name__ == '__main__':
#     directory_name = "/Users/bpandit/Documents/GitHub/cluster_data/"
#     image_paths, data = images_to_numpy(directory_name)
#     labels = spectralClustering(data)
#     makeCluster(labels, image_paths)
