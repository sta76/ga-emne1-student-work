packing_list = ["cpu", "gpu", "minne", "tastatur"]
for i in packing_list:
    print(i, end=" ")
print()
packing_list.append("mus")
print(packing_list)
print()
packing_list.remove("minne")
print(packing_list)