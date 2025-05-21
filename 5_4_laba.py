import random
correct = 0
errors = 0

while errors < 3:
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    x = n1 + n2

    answer = int(input(f"{n1} + {n2} = "))

    if answer == x:
        correct += 1
        print("Правильно!")
    else:
        errors += 1
        print("Неправильно!")

print("Игра окончена. Правильный ответов:", correct)