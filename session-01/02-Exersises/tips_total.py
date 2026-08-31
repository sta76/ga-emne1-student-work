cost = float(input("Enter the cost of the item: "))
tip = (cost * 15)/100
cost_including_tip = cost + tip

print(f"If the item cost {cost:.2f} 15% tip is {tip:.2f} that gives a total of {cost_including_tip:.2f}")
