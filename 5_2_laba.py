str2 = ""
while True:
    w = input("enter words or stop ")
    if w.lower() == "stop":
        break
    str2 += w + " "
print("Результат:", str2.strip())