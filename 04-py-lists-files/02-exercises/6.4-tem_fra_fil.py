import numbers
from pathlib import Path
import math

data_directory = Path(__file__).parent.parent / "data"
temp_directory = data_directory / "temperatures.txt"
print(temp_directory.exists())
temp_list = []
try:
    with open(temp_directory, "r", encoding="utf-8") as file:
        for t in file:
            temp_list.append(float(t))
    print(temp_list)
except FileNotFoundError:
    print(f"Could not open file: {temp_directory}")

count = 0
for temp in temp_list:
     count += 1
     print(f"Temperaturen er: {temp:.2f} grader")
print()
print(f"Det er {count} antall målinger")
print(f"Den laveste temperaturen er: {min(temp_list)} grader\n"
      f"Den høyeste er: {max(temp_list)} grader\nGjennomsnittet er: {(sum(temp_list)/len(temp_list)):.2f} grader")