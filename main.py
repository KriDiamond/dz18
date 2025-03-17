def check_oportunity_to_vote(person_age, person_citizenship, person_disqualification):
    if person_age >= 18 and person_citizenship == True and person_disqualification == False:
        result = True
    else:
        result = False
    return result


try:
    age = int(input("Введите ваш возраст: "))
    answer = (input("Имеется ли у вас гражданство страны (да/нет): ")).lower()
    if answer == 'да':
        is_citizen = True
    else:
        is_citizen = False
    answer = (input("Имеется ли у вас дисквалификация, например из-за судимости (да/нет): ")).lower()
    if answer == 'да':
        is_disqualificated = True
    else:
        is_disqualificated = False
    if check_oportunity_to_vote(age, is_citizen, is_disqualificated):
        result = 'Вы допущены до голосования. Поздравляем!'
    else:
        result = 'Вы не допущены до голосования.'
except ValueError:
    print("Ошибка: Не верный формат данных!")
else:
    print(f"Результат: {result}")
finally:
    print('Программа завершила работу.')