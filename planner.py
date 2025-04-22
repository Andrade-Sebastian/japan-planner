import collections, argparse, json

class Planner:
    def __init__(self, all_activities):
        self.all_activities = all_activities
def rank_activities(all_activities):
    for sublist in all_activities:
        for item in sublist:
            print(item)