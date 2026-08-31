minutes = int(input("Enter a value in minutes: "))

hour = minutes // 60
minutes_left = minutes % 60
print(f"{minutes} minutes is {hour} hour and {minutes_left} minutes")
