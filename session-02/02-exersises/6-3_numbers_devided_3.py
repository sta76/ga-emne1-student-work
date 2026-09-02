count = 0
for number in range(1, 100):
    if number % 3 == 0 and 20 < number < 80:    # if number % 3 == 0 and number > 20 and number < 80:
        count += 1
        print(number)
print(count)
