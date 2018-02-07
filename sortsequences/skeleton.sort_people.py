from datastubs import PEOPLE_LIST

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
    sort by age in ascending order
    """
    # fill it out

def oldest():
    """
    sort by age in descending order
    """
    # fill it out


def name_reverse_alpha():
    # fill it out


def country_then_age():
    # fill it out
