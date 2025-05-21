spis = [2, 4, 6, 8, 9]

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

days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

week_k = int(input("Сколько выходных на неделе вы хотите? "))

if week_k < 0 or week_k > 7:
    print("Неверное количество выходных. Пожалуйста, введите число от 0 до 7.")
else:

    weekends = days[-week_k:]  # срезаем последние выходные дни
    workdays = days[:-week_k]  # оставшиеся

    print(f"Ваши выходные дни: {', '.join(weekends)}")
    print(f"Ваши рабочие дни: {', '.join(workdays)}")


numbers = [5, 10, 15, 20, 25]
user_number = int(input("Введите число: "))

if user_number in numbers:
    print(f"Поздравляю, Вы угадали число! ({user_number} присутствует в списке)")
else:
    print("Нет такого числа!")

print("Исходный список:", numbers)


group_1 = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Попов", "Чернов", "Федоров", "Лазурин", "Лебедев", "Смирнов"]
group_2 = ["Андреев", "Зайцев", "Жуков", "Головкин", "Брюхов", "Соколов", "Григорьев", "Иванов", "Сергеев", "Ковалев"]

team = tuple(group_1[:5] + group_2[:5])

print("Исходный список студентов группы 1:")
for student in group_1:
    print(student)

print("\nИсходный список студентов группы 2:")
for student in group_2:
    print(student)

print("\nКоманда:")
for member in team:
    print(member)

print("\nДлина команды:", len(team))

sorted_team = sorted(team)
print("\nОтсортированная команда:")
for member in sorted_team:
    print(member)

count_ivanov = team.count("Иванов")
if "Иванов" in team:
    print(f"\nСтудент 'Иванов' входит в команду и встречается {count_ivanov} раз.")
else:
    print("\nСтудент 'Иванов' не входит в команду.")