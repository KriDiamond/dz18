def check_oportunity_to_vote(person_age, person_citizenship, person_disqualification):
    if person_age >= 18 and person_citizenship == True and person_disqualification == False:
        result = True
    else:
        result = False
    return result