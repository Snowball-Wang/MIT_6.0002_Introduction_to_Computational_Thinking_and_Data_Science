###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows_dict = {}
    # Use with-open method to deal with text file
    with open(filename, 'r') as f:
        for line in f:
            # Get rid of '\n' in each line
            line = line.strip('\n')
            # Get cow name and weight and store them in the dictionary
            key, value = line.split(',')
            # Transfer the str type of value into int type
            cows_dict[key] = int(value)

    return cows_dict


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Make a copy for cows dict
    cows_copy = cows.copy()
    # The list that contains all trips
    trip_list = []

    # Judge whether the dict is empty, if not, go on
    while len(cows_copy) != 0:
        # The list for one trip
        trip = []
        left = limit
        while left > 0:
            # Get all weights that satisfy the condition that there are left space
            weight_list = [v for k, v in cows_copy.items() if v <= left]
            # If weight_list is not empty, go on
            if weight_list:
                max_weight = max(weight_list)
                # There are probably more than one cows satisfy the max_weight, just pick up the first one
                cows = str([k for k,v in cows_copy.items() if v == max_weight][0])
                trip.append(cows)
                del cows_copy[cows]
                # Update the left space
                left = left - max_weight
            else:
                break
        trip_list.append(trip)

    return trip_list



# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
