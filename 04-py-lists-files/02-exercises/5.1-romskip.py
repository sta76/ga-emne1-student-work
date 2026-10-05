
spaceship = {"name": "Enterprise", "captain": "Kirk", "speed": "warp 10", "operational": "starfleet"}

print(spaceship)
print()

print(f"Name: {spaceship['name']}, Captain: {spaceship['captain']}")
spaceship['speed'] = 'warp 8'
spaceship['title'] = 'Star Trek'
print(spaceship)

for ship in spaceship.items():
    print(ship)

