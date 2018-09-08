import random
import collections

def sampleFromDict(src_dict, num_of_samples_per_key):
    """
    For a dictionary which maps keys to arrays, this method returns a new dictionary
    where the keys map to arrays that have been created by sampling randomly from the
    original array.
    If array that is being sampled from has less elements than the num_of_samples_per_key
    requested, the randomly sampled array will contain lesser elements than requested.
    If data type in mapped arrays are not hashable, the elements in the
    returned array might not be unique.

    Args:
    src_dict : dictionary to sample from
    number_of_samples_per_key : (int) number of samples requested for each key
    """
    sampled_data = {}
    for key in src_dict:
        src_array = src_dict[key]
        sampled_data[key] = sampleFromArray(src_array, num_of_samples_per_key)
    return sampled_data


def sampleFromArray(array, num_of_samples):
    """
    Randomly sample num_of_samples units from the array.
    If num_of_samples > len(array), the entire array is returned.

    Args:
    array: generic list to sample from.
    num_of_samples: number of samples from array
    """

    # if not enough to start with, no trimming
    if len(array) < num_of_samples:
        return array

    if not isinstance(array[0], collections.abc.Hashable):
        return sampleArrayStoringUnhashable(array, num_of_samples)
    # set will store random samples from array
    # created a set so that while sampling randomly, a single element
    # is not sampled more than once
    random_set = set()
    while len(random_set) != num_of_samples:
        random_unit = array[random.randrange(len(array))]
        random_set.add(random_unit)

    return list(random_set)

def sampleArrayStoringUnhashable(array, num_of_samples):
    """
    Randomly sample num_of_samples units from the array which
    is not necessarily hashable.

    Args:
    array: generic list to sample from.
    num_of_samples: number of samples from array
    """
    return [array[random.randrange(len(array))]
            for sample in range(num_of_samples)]
