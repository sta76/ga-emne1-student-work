pris = float(input("Hva koster varen?: "))

if pris >= 1000:
    rabatt = 0.20

elif pris >= 500:
    rabatt = 0.1

else:
    rabatt = 0

pris_med_rabatt = pris * (1 - rabatt)
print(f"Pris med rabatt: {pris_med_rabatt}")