stored_goals = []
while True:
    print("\n==== Walk Goal Tracker ====\n")
    print("1. Create a goal")
    print("2. Edit a goal")
    print("3. Delete a goal")
    print("4. Show all goals")
    print("5. Quit")
    try:
        choice = int(input("\nEnter choice: "))
        if choice < 1 or choice > 5:
            print("Please enter number from 1 to 5")
            continue
    except ValueError:
        print("Please enter an integer")
        continue
    match choice:
        case 1:
            print("\n===========================\n")
            title_of_goal = input("Enter goal title: ")
            distance = float(input("Enter distance for each day: "))
            days = int(input("Enter amount of days: "))
            goal = {"title": title_of_goal,
                    "distance": distance,
                    "days": days,
                    "total distance": distance * days}
            stored_goals.append(goal)
        case 2:
            print("\n===========================\n")
            for goal in stored_goals:
                print(goal)
            print("\n===========================\n")
            goal_to_edit = input("Enter title of goal to edit: ")
            for index, goal in enumerate(stored_goals):
                if goal_to_edit.lower() == goal["title"].lower():
                    print(goal)
                    print("1. goal title")
                    print("2. distance")
                    print("3. days")
                    while True:
                        try:
                            what_to_edit = int(input("\nwhat would you like to edit?: "))
                            if what_to_edit < 1 or what_to_edit > 3:
                                print("Please enter number from 1 to 3")
                                continue
                            break
                        except ValueError:
                            print("Please enter an integer")
                            continue
                    match what_to_edit:
                        case 1:
                            goal = {"title": input("Enter new title: "),
                                    "distance": stored_goals[index]["distance"],
                                    "days": stored_goals[index]["days"],
                                    "total distance": stored_goals[index]["distance"] * stored_goals[index]["days"]}
                            stored_goals[index] = goal
                        case 2:
                            distance = float(input("Enter new distance for each day: "))
                            goal = {"title": stored_goals[index]["title"],
                                    "distance": distance,
                                    "days": stored_goals[index]["days"],
                                    "total distance": distance * stored_goals[index]["days"]}
                            stored_goals[index] = goal
                        case 3:
                            days = int(input("Enter new amount of days: "))
                            goal = {"title": stored_goals[index]["title"],
                                    "distance": stored_goals[index]["distance"],
                                    "days": days,
                                    "total distance": stored_goals[index]["distance"] * days}
                            stored_goals[index] = goal
            print("edit successful")
        case 3:
            print("\n===========================\n")
            for goal in stored_goals:
                print(goal)
            goal_to_delete = input("\nEnter title of goal to delete: ")
            for index, goal in enumerate(stored_goals):
                if goal_to_delete.lower() == goal["title"].lower():
                    del stored_goals[index]
                    print("delete successful")
        case 4:
            print("\n===========================\n")
            for goal in stored_goals:
                print(goal)
        case 5:
            print("\n===========================\n")
            print("shutting down program")
            break