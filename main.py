try:
    num1 = int(input("\nВведите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 + num2
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Результат сложения: {result}")

try:
    num3 = int(input("\nВведите первое число: "))
    num4 = int(input("Введите второе число: "))
    result = num3 - num4
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Результат вычитания: {result}")

try:
    num5 = int(input("\nВведите первое число: "))
    num6 = int(input("Введите второе число: "))
    result = num5 * num6
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Результат умножения: {result}")

try:
    num7 = int(input("\nВведите первое число: "))
    num8 = int(input("Введите второе число: "))
    result = num7 / num8
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
else:
    print(f"Результа деленият: {result}")
