numbers = [20,
           34,
           10,
           45,
           56,
           67,
           76,
           86,
           50
           ]
count = 0
for num in numbers:
    if num > 50:
        print(num)
        count +=1
    else:
        continue
print(f"Det er {count} tall over 50 i listen")