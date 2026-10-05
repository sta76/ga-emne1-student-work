color = (255, 4, 6)
print(f"RGB kode er: R:{color[0]} G:{color[1]} B:{color[2]}")
color_list = [
    (40,70,255),
    (205,80,90),
    (30,55,79)
]

for c in color_list:
    print(f"RGB-verdi:{c}")

#   KI forslag under
# # Del 1: Én fargetuple (Rød, Grønn, Blå)
# color = (255, 100, 50)
#
# # Skriv ut verdiene i en forklarende setning
# print(f"Fargekoden har rød={color[0]}, grønn={color[1]} og blå={color[2]}.")
#
# # Del 2: En liste med tre forskjellige fargetupler
# farger = [
#     (255, 0, 0),     # Rød
#     (0, 255, 0),     # Grønn
#     (0, 0, 255)      # Blå
# ]
#
# # Skriv ut hver tuple i en løkke
# for farge in farger:
#     print(f"RGB-verdi: {farge}")