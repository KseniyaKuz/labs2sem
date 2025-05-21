numbers = list(range(10, 51, 5))
user_number = int(input("Введите число: "))

if user_number in numbers:
    print(f"Поздравляю, Вы угадали число! ({user_number} присутствует в списке)")
else:
    print("Нет такого числа!")

print("Исходный список:", numbers)