'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''

from collections import namedtuple
from collections import Counter
from collections import defaultdict
from ways import load_map_from_csv

import sys


def count_road_types(roads):
    road_type_lst = []
    road_type_set = set()
    # for i in roads.junctions():
    #     for j in i.links:
    #         road_type_lst.append(j.highway_type)

    road_type_lst += [j.highway_type for i in roads.junctions() for j in i.links]

    print('road_type_lst is: ',road_type_lst)
    return road_type_lst



def calc_branch_out(roads, number_of_junctions):
    branch_out = defaultdict(lambda: 0)
    for link in roads.iterlinks():
        print(link)
        branch_out[link.source] += 1
    max_branching_factor = 0
    min_branching_factor = sys.maxsize
    branching_out_sum = 0
    for junction in roads.junctions():
        v = branch_out[junction.index]
        if v < min_branching_factor:
            min_branching_factor = v
        if v > max_branching_factor:
            max_branching_factor = v
        branching_out_sum += v
    print(Counter(branch_out))
    return min_branching_factor, max_branching_factor, branching_out_sum/number_of_junctions


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    link_num = 0
    max_link_dist = 0
    min_link_dist = sys.maxsize
    avg_dist = None
    dist_sum = 0
    number_of_junctions = len(roads.junctions())

    for i in roads.junctions():
        print('Junction: ', i)
        link = i.links
        print('Links : ', link)
        for j in link:
            Counter(j)
            #print('link dist is ', j[2])
            print('link dist is ', j.distance)
            dist = j.distance
            dist_sum = dist_sum + dist
            if dist > max_link_dist:
                max_link_dist = dist
            if dist < min_link_dist:
                min_link_dist = dist
        print(' ')
        link_num += len(i.links)
        avg_dist = dist_sum/link_num

    return {
        'Number of junctions': number_of_junctions,
        'Number of links': link_num,
        'Outgoing branching factor': Stat(*calc_branch_out(roads, number_of_junctions)),
        'Link distance': Stat(max_link_dist, min_link_dist, avg_dist),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': Counter(count_road_types(roads)),  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))

        
if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()
