import datetime
input_goal = input("Input what is your goal and when id your deadline, separated by semicolon: (example goal:dd.mm.yyyy) ")

input_list = input_goal.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

today_date = datetime.datetime.today()

time_till = deadline_date - today_date

print(f"Time remaining for your goul: {goal} is {time_till.days}")
