import numpy as np
import scipy
from sklearn.decomposition import RandomizedPCA
from scipy.cluster.vq import whiten
from sklearn.cluster import KMeans
from scipy.cluster.vq import vq

def kmeans(X, num_clusters):
    """
    Performs K-Means clustering on the data X

    Args:
    X: (n, k) dimensional numpy array representing n data points
               and k features
    num_clusters: number of clusters to form
    """
    kmeans = KMeans(num_clusters)
    kmeans.fit(X)
    # return the cluster center and the labels associated with the data points
    return kmeans.cluster_centers_, kmeans.labels_

def spectralClustering(data):
    """
    Performs spectral clustering on data.

    Args:
    data: data to be clustered in the form of a (n, k)
          numpy array. n is the number of data points
          and k is the number of features (pixels if the data is an image)
    """

    pca = RandomizedPCA(n_components=32) #reducing feature dimension to 32
    projected = pca.fit_transform(data)
    n = len(projected) # number of data points

    # spectral clustering
    # k-means on eigenvectors of the similarity matrix
    # calculating the similarity matrix
    S = np.array([[ np.sqrt(np.sum((projected[i]-projected[j])**2))
                    for i in range(n) ] for j in range(n)], 'f')

    # create symmetric normalized graph Laplacian matrix
    rowsum = np.sum(S,axis=0)
    D = np.diag(1 / np.sqrt(rowsum))
    I = np.identity(n)
    L = I - np.dot(D,np.dot(S,D))

    # eigenvectors of Laplacian (L)
    U,sigma,V = np.linalg.svd(L) # singular-value-decomposition

#    kmax = int(np.sqrt( len(image_data)/2.0 ))  # default in many packages

    kmax = 6 #number of clusters

    # first k eigenvectors as features
    features = whiten(np.array(V[:kmax]).T)

    # centroids, distortion = kmeans(features,kmax)
    centroids, labels = kmeans(features, kmax)
    code, distance = vq( features, centroids ) #scipy.cluster.vq
    return labels
