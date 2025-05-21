spis = [2, 4, 6, 8, 9, 2]

prov = set()
dub = []

for i in spis:
    if i in prov:
        dub.append(i)
    else:
        prov.add(i)

if dub:
    print(f"Повторяющиеся элементы: {dub}")
else:
    print("Повторяющихся элементов нет.")