guest = ["Kermit", "Miss Piggy", "Gonzo"]
print(guest)

print("\n---\n")

mixed_bag = ["Tomas", 52, True]
print(mixed_bag)

print("\n---\n")
print(guest[0])
print(guest[1])
print(guest[-1]) # Siste element

print("\n---\n")

guest.append("Animal") # Legger til element
print(guest)
guest.remove("Gonzo")
print(guest)
print(len(guest))
print("\n---\n")

for g in guest:
    print(f"Welcome, {g}")
print("\n---\n")

scores = [72, 88, 91, 65]

print(len(scores))
print(sum(scores))

average = sum(scores) / len(scores)
print(f"average: {average}")
print(min(scores))
print(max(scores))
print("\n---\n")

guest.insert(1, "Camilla") # Sett inn nytt element på index 1
print(guest)