from os import name

cue_list = ["Per", "Pål", "Espen", "Gunnar"]

print(f"{cue_list[0]}, {cue_list[-1]}")
for name in cue_list:
    print(name, end=", ")
print()
cue_list.remove("Per")
cue_list.append("Ole")
for name in cue_list:
    print(name, end=", ")