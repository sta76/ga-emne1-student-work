prices = [100,
          150,
          300,
          359,
          1245
          ]
for price in prices:
    print(f"{price} med 20 % rabatt er : {(price * 0.8):.2f}")
print()
print(f"Summen av alle prisene er: {sum(prices)}")
