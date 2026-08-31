distance = int(input("Enter the driving distance in km: "))
fuel_per_100_km = float(input("Enter fuel consumption in liter per 100 km: "))
fuel_price = float(input("Enter the fuel price per liter: "))

fuel_consumption = (distance / 100) * fuel_per_100_km
distance_price = fuel_consumption * fuel_price

print(f"For a distance of {distance} km, you use {fuel_consumption} liter at a cost of {distance_price} kr")
