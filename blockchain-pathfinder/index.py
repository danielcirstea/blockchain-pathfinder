from __mocks__ import simple_graph_mock
from pq_profile import Profile
from guppy import hpy
import csv

with open('input_data/graph9.csv') as f:  # change 'input_data/graph9.csv' to whatever input is needed
    data = [(line['from'], line['to']) for line in csv.DictReader(f, skipinitialspace=True)][:50]  # limit records here
    result = list(zip(*data))


def mine_patterns(p, q, t):
    profile = Profile(result, p, q, t)
    patterns = profile.pq_gram_profile()
    return patterns


def pq_gram_distance(profile1, profile2):
    intersections, unions = 0, len(profile1) * 2
    for k in profile1:
        if k in profile2:
            intersections += 1
    return 1 - 2 * (intersections / unions)


print(mine_patterns(2, 3, 0))
