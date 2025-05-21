a = int(input("Введите количество слов:"))
str1 = ""
for i in range(a):
    word = input(f"Введите слово {i+1}: ")
    str1 += word + " "

print("Результат:", str1.strip())