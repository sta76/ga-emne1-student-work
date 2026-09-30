temperature = [11,
               14,
               9,
               15,
               6,
               20,
               10
               ]
for temp in temperature:
    if temp < 10:
        print(f"The temperatur is {temp} degrees, it's a cold day")
    else:
        print(f"The temperature is {temp} degrees")
print(f"The lowest temp is {min(temperature)} degrees, den høyeste {max(temperature)} degrees and average is {(sum(temperature)/len(temperature)):.2f} degrees")