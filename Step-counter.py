print("🏃‍♂️ Step Counter 🏃‍♂️" )
daily_goal = int (input("Enter your daily step goal: "))
current_steps = int(input("How many steps have you taken today? "))

remaining = daily_goal - current_steps

if remaining > 0:
    print(f"You have {remaining} steps left to reach your daily goal of {daily_goal} steps.")
else:
    print("Congratulations! You've reached your daily step goal of {daily_goal} steps!")
