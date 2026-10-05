movies =["Batman Begins",
         "Batman - The dark night",
         "Batman - The dark night rises",
         "Star Wars - A new hope",
         "Star Wars- The empire strikes back"
         ]

print(movies[0])
print(movies[2])
print(movies[-1])
print()
for movie in movies:
    print(movie)
print()
movies[1] = "Ringenes Herre"

for movie in movies:
    print(movie)