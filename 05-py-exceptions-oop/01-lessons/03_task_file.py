from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"  # Absulutt path
path = data_folder / "report.txt"
print(path)

try:
    # with open(path, "r", encoding = "utf-8") as file:
    with path.open("w", encoding="utf-8") as file:
        text = file.write("Practice report\n")
    print("Practice report")
except FileNotFoundError:
    print(f"Error, could not open file: {path}")
except PermissionError:
    print("Error, no permission to write here")
