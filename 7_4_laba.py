group_1 = ["Волков", "Морозов", "Виноградов", "Мельников", "Егоров", "Щербаков", "Зимин", "Крылов", "Денисов"]
group_2 = [ "Алексеев", "Борисов", "Орлов", "Титов", "Романов", "Павлов", "Николаев", "Васильев", "Кузьмин"]

team = tuple(group_1[:5] + group_2[:5])  # преобразуем списки в кортежи

print("Исходный список студентов группы 1:")
for student in group_1:
    print(student)

print("\nИсходный список студентов группы 2:") # \n перевод строки вниз
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