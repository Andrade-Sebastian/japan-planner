##COVERAGE REPORT##
"""
Name              Stmts   Miss  Cover
-------------------------------------
planner.py           24      1    96%
test_planner.py      39      1    97%
-------------------------------------
TOTAL                63      2    97%
"""

import unittest
from planner import rank_activities
class Test_Planner(unittest.TestCase):
    #Test duplicate names, capitals vs lowercase, 

    def testTotalActivities(self):
        input_data = [["sushi", "hiking", "temple"], ["disney", "sushi", "sumo"], ["sushi", "temple", "boating"]]
        result = rank_activities(input_data)
        self.assertGreater(result["sushi"],result["sumo"])
        self.assertGreater(result["temple"], result["boating"])
        self.assertEqual(len(result), 6)


    def testCaseSensitivity(self):
        input_data = [["Ramen", "SUSHI", "Onsen"],["RaMeN", "Sushi", "ONSEN"]]
        result = rank_activities(input_data)

        self.assertIn("onsen", result)
        self.assertIn("sushi", result)
        self.assertIn("ramen", result)

    def testTrailingSpaces(self):
        input_data = [[" ramen", "     sushi", "disney  "], ["ramen", "sushi", "disney"]]
        result = rank_activities(input_data)

        self.assertEqual(len(result), 3)
        self.assertIn("ramen", result)
        self.assertIn("sushi", result)
        self.assertIn("disney", result)

    def testTieBreaker(self):
        input_data = [["sushi", "hiking", "temple"], ["temple", "sushi", "hiking"], ["hiking", "temple", "sushi"]]
        result = rank_activities(input_data)

        keys = list(result.keys())
        expected = sorted(keys)
        self.assertEqual(keys, expected)

    def testSimilarInputs(self):
        input_data = [["sushi", "disney", "sumo"],["Sushi ", "Disney ", "Sumo "],[" SuShI", "DisNeY", "SUmO"]]
        result = rank_activities(input_data)

        self.assertIn("sushi", result)
        self.assertIn("disney", result)
        self.assertIn("sumo", result)

        self.assertGreater(result["disney"], 0)
        self.assertGreater(result["sushi"], 0)
        self.assertGreater(result["sumo"], 0)


if __name__ == '__main__':
    unittest.main()
        

