from planner import rank_activities
def main():
    all_activities = []

    print(r"""
  __     ______     ______   ______     __   __        ______   __         ______     __   __     __   __     ______     ______    
  /\ \   /\  __ \   /\  == \ /\  __ \   /\ "-.\ \      /\  == \ /\ \       /\  __ \   /\ "-.\ \   /\ "-.\ \   /\  ___\   /\  == \   
 _\_\ \  \ \  __ \  \ \  _-/ \ \  __ \  \ \ \-.  \     \ \  _-/ \ \ \____  \ \  __ \  \ \ \-.  \  \ \ \-.  \  \ \  __\   \ \  __<   
/\_____\  \ \_\ \_\  \ \_\    \ \_\ \_\  \ \_\\"\_\     \ \_\    \ \_____\  \ \_\ \_\  \ \_\\"\_\  \ \_\\"\_\  \ \_____\  \ \_\ \_\ 
\/_____/   \/_/\/_/   \/_/     \/_/\/_/   \/_/ \/_/      \/_/     \/_____/   \/_/\/_/   \/_/ \/_/   \/_/ \/_/   \/_____/   \/_/ /_/ 
                                                                                                                                    
""" )
    print("Welcome to the Japan Activity Planner! This program was created to prioritize the most popular activies to do in Japan.")
    print("Please insert 10 activities you would want to do in Japan.")
    for i in range(1,4): # Loops hree times for three peaople
        print(f"Person {i}, enter your activities now.")
        user_activities = []
        for j in range(1, 11):
            activity = input(f"Activity {j+1}: ").strip().lower()
            user_activities.append(activity)
        print(f"Person {i} activities: ", user_activities)
        all_activities.append(user_activities)
    print("Great here are the activities entered by each person: ", all_activities)
    print("Now ranking each activity...")
    ranked = rank_activities(all_activities)
    
if __name__ == "__main__":
    main()