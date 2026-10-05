opening_hours = ("Mandag","kl.7", "kl.15.30",
                 "Tirsdag", "kl.7", "kl.15.30",
                 "Onsdag", "kl.8.30", "kl.17.30")

for i in range(0, len(opening_hours),3):    # hopper med steg på 3
    print(f"Vi åpner {opening_hours[i]} {opening_hours[i + 1]} og stenger {opening_hours[i + 2]}")

print()
for i in range(0, len(opening_hours), 3):
    dag, aapner, stenger = opening_hours[i:i+3] # Pakker it en bit på 3 (fra i til men ikke med i + 3) og ligger de i variabler
    print(f"Vi åpner {dag} {aapner} og stenger {stenger}")


