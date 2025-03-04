try:
    num1 = int(input("\nВведите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(
        "Выберите номер 1, для операции сложения; 2, для операции вычитания; \n               3, для операции умножения; 4, для операции деления;")
    num3 = int(input("Введите порядковый номер операции: "))
    match num3:
        case 1:
            result = num1 + num2
        case 2:
            result = num1 - num2
        case 3:
            result = num1 * num2
        case 4:
            result = num1 / num2
        case _:
            result = "-"
            print("Указанный номер не соответсвует списку операций :(")
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(f"Результат операции: {result}")
