from planner import rank_activities
def main():
    NUM_PEOPLE = 3
    ACTIVITIES_PER_PERSON = 10
    all_activities = []

    print(r"""
  __     ______     ______   ______     __   __        ______   __         ______     __   __     __   __     ______     ______    
  /\ \   /\  __ \   /\  == \ /\  __ \   /\ "-.\ \      /\  == \ /\ \       /\  __ \   /\ "-.\ \   /\ "-.\ \   /\  ___\   /\  == \   
 _\_\ \  \ \  __ \  \ \  _-/ \ \  __ \  \ \ \-.  \     \ \  _-/ \ \ \____  \ \  __ \  \ \ \-.  \  \ \ \-.  \  \ \  __\   \ \  __<   
/\_____\  \ \_\ \_\  \ \_\    \ \_\ \_\  \ \_\\"\_\     \ \_\    \ \_____\  \ \_\ \_\  \ \_\\"\_\  \ \_\\"\_\  \ \_____\  \ \_\ \_\ 
\/_____/   \/_/\/_/   \/_/     \/_/\/_/   \/_/ \/_/      \/_/     \/_____/   \/_/\/_/   \/_/ \/_/   \/_/ \/_/   \/_____/   \/_/ /_/ 
                                                                                                                                    
""" )
    print("Welcome to the Japan Activity Planner! This program was created to prioritize the most popular activies to do in Japan.")
    print(f"Please insert {ACTIVITIES_PER_PERSON} activities you would want to do in Japan.")
    for i in range(1,NUM_PEOPLE + 1): # Loops hree times for three peaople
        print(f"Person {i}, enter your activities now.")
        user_activities = []
        for j in range(1, ACTIVITIES_PER_PERSON + 1):
            while True:
                activity = input(f"Activity {j}: ").strip().lower()
                if activity:
                    break
                print("Activity cannot be empty. Please enter something...")
            user_activities.append(activity)
        print(f"Person {i} activities: ", user_activities)
        all_activities.append(user_activities)
    print("Great! Here are the activities entered by each person:")

    for i, activity in enumerate(all_activities, 1):
        print(f"Person{i}: {activity}")
    print("Now ranking each activity...")
    ranked = rank_activities(all_activities)
    print("\n Final Ranking:")
    for i, (activity, points) in enumerate(ranked.items(), 1):
        print(f"{i}. {activity.capitalize()} - {points} pts")
        
if __name__ == "__main__":
    main()