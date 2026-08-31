pris = float(input("Hva koster varen du vil kjøpe: "))
rabatt = int(input("Hvor mange prosent er rabatten: "))

sum_rabatt = pris * (rabatt / 100)
rabattert_pris = pris - sum_rabatt
print(f"Koster varen kr {pris}, vil rabatten utgjøre kr {sum_rabatt:.2f} og rabattert pris blir kr {rabattert_pris:.2f}")