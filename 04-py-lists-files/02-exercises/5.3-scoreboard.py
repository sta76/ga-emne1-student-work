scoreboard = {'espen': 200, 'ståle': 220, 'per': 120, 'pål': 300}
print(scoreboard['espen'])
scoreboard['espen'] = 230
scoreboard['arne'] = 100
print()
for item in scoreboard.items():
    print(f"{item[0]} fikk en score på {item[1]}")