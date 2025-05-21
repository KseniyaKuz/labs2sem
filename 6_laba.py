def z1(number):
    return number % 3 == 0

def z2():
    try:
        vv = input("Введите число для деления 100: ")
        number = float(vv)
        result = 100 / number
        return result
    except (ValueError, ZeroDivisionError):
        return "Ошибка"

def z3(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        posl = year % 100
        return day * month == posl
    except ValueError:
        return "Ошибка: Введите дату в формате dd.mm.yyyy."

def z4(ticket):
    n = len(ticket) // 2
    return sum(int(ticket[i]) for i in range(n)) == sum(int(ticket[i]) for i in range(n, len(ticket)))

def main():
    while True:
        print("Выберите программу:")
       
        print("0 - Выход")
        choice = input("Введите номер программы: ")

        if choice == '1':
            number = int(input("Введите число: "))
            print("Делится на 3." if z1(number) else "Не делится на 3.")
        elif choice == '2':
            print(z2())
        elif choice == '3':
            vv = input("Введите дату (dd.mm.yyyy): ")
            result = z3(vv)
            print("Магическая дата!" if result is True else "Не магическая дата" if result is False else result)
        elif choice == '4':
            ticket = input("Введите номер билета: ")
            print("Билет счастливый!" if z4(ticket) else "Билет не счастливый.")
        elif choice == '0':
            break
        else:
            print("Некорректный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()

