# japan-planner

To preface, as graduation looms, my friends and I are planning a trip to Japan a few days after we graduate. This project will help us decide what activities to prioritize when we arrive there and which activities to drop during the duration of our trip. The Japan group activity planner will be a Python-based command-line interface application that will help us collectively decide on which activities to participate in and plan during our trip. Each person will enter a list of activities they are interested in, the app will compile all of the answers, scores, and ranks the most common interests based on frequency. The results will then be ranked and will illustrate a clear list of activities everyone is most excited about.

# Functionality and Technologies That Will Be Used
Will be built with Python 3


Will use these libraries: collections, argparse, json 


CLI will prompt users to type in their top 10 activities each


Will compile activities across users


Will assign points based on frequency (most common gets highest score)


Outputs a final ranked activity list


# Unit Test Coverage Plan
To achieve at least 75%, the components I will be testing will be input validation, duplicate detection (if two people type in the same activity, that activity will be placed higher in the list), case sensitivity (activities where one is typed with a capital and one is typed without a capital will count as the same activity), scoring and point allocation logic, and sorting and final output formatting. To measure the test coverage, I will use Python’s unittest and coverage report tools. Tests will be written to isolate each function to achieve a high test coverage.



# Integration Test Plan
All three users enter valid lists, make sure it is stored correctly


Activities entered by multiple people, make sure they are scored with highest points


Activities with different casing ("Ramen", "ramen"), make sure they are stored and merged as one.


User enters fewer or more than 10 items, make sure the app still functions


Output is created with final ranked list

# Source Code Centralization and CI Plan
Code will be pushed to a repository on GitHub.
I will be using GitHub Actions to run unittest on all pushes and pull requests and generate test coverage reports.

# Build and Deployment Automation Plan
For the build process and automation plan, I will be using PyInstaller to generate a standalone executable. PyInstaller ensures that the app can be run without installing Python. This can be useful for travel with limited Wi-Fi or internet access.
