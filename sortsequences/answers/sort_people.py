from datastubs import PEOPLE_LIST

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p):
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
    sort by age in ascending order
    """
    return sorted(PEOPLE_LIST, key=lambda x: x['age'])

def oldest():
    """
    sort by age in descending order
    """
    def myfoo(m):
        return m['age']

    return sorted(PEOPLE_LIST, key=myfoo, reverse=True)


def name_reverse_alpha():
    return sorted(PEOPLE_LIST, key=lambda x: x['name'], reverse=True)


def country_then_age():
    return sorted(PEOPLE_LIST, key=lambda x: (x['country'], x['age']))
