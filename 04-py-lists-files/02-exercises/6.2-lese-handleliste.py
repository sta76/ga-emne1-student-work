from  pathlib import Path

print(f"Current directory is {Path.cwd()}")

data_directory = Path("..") / "data"

shopping_list_path = data_directory / "shopping_list.txt"

shopping_list = []
with open(shopping_list_path, "r", encoding="utf-8") as file:
    for line in file:

        shopping_list.append(line.strip())
print(shopping_list)
print()
for item in shopping_list:
    print(item)