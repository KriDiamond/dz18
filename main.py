def check_oportunity_to_vote(person_age, person_citizenship, person_disqualification):
    if person_age >= 18 and person_citizenship == 'да' and person_disqualification == 'нет':
        result = 'Вы допущены до голосования. Поздравляем!'
    else:
        result = 'Вы не допущены до голосования.'
    return result


try:
    age = int(input("Введите ваш возраст: "))
    is_citizen = (input("Имеется ли у вас гражданство страны (да/нет): ")).lower()
    is_disqualificated = (input("Имеется ли у вас дисквалификация, например из-за судимости (да/нет): ")).lower()
except ValueError:
    print("Ошибка: Не верный формат данных!")
else:
    print(f"Результат: {check_oportunity_to_vote(age, is_citizen, is_disqualificated)}")
finally:
    print('Программа завершила работу.')