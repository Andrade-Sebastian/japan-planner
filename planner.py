import collections, argparse, json
from collections import Counter

class Planner:
    def __init__(self, all_activities):
        self.all_activities = all_activities
def rank_activities(all_activities):
    flat_list = []
    for sublist in all_activities:
        for item in sublist:
            print(item)
            flat_list.append(item.lower().strip())
    print(f"Here is the flat list {flat_list}" )
    count = Counter(flat_list)
    print(f"Here is the count {count}")
    rank =sorted(count.items(), key=lambda x: -x[1])
    print("HERE IS THE RANK",rank)

    score_map = {}
    score = len(rank)
    print("HERE IS THE SCORE", score)
    for activity, _ in rank:
        score_map[activity] = score
        score -= 1

    print("Finally the score_map", score_map)
    return score_map

            