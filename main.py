def max_number(a, b):
    if b>a: a=b
    return a


def empty_function():
    pass


def even_numbers( n ):
    for i in range (0, n + 1, 2):
        yield i


def test_max_number():
    assert max_number(3, 5) == 5, "Ошибка: максимум из (3, 5) должен быть равен 5"
    assert max_number(-3, -5) == -3, "Ошибка: максимум из (-3, -5) должен быть равен -3"
    assert max_number(-3, 0) == 0, "Ошибка: максимум из (-3, 0) должен быть равен 0"
    assert max_number(5, 5) == 5, "Ошибка: максимум из (5, 5) должен быть равен 5"


print(max_number(3,5))
for even in even_numbers(6):
    print(even)
test_max_number()
print("Все тесты пройдены!")
