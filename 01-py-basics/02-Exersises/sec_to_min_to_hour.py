seconds = int(input("Enter in seconds: "))

hours = seconds // 3600
min = (seconds -  (hours * 3600)) // 60
sec_left = seconds % 60

print(f"{seconds} is {hours} hour, {min} minutes and {sec_left} seconds")
