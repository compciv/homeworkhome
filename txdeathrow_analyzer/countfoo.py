from collections import defaultdict
from scraper import get_inmate_data

def count_women():
    the_count = 0
    for row in get_inmate_data():
        if row['gender'] == 'F':
            the_count += 1
    return the_count


def count_by_gender():
    gendercount = {}
    for inmate in get_inmate_data():
        gprop = inmate['gender']
        if gendercount.get(gprop):
            gendercount[gprop] += 1
        else:
            gendercount[gprop] = 1
    return gendercount

def count_young_offenders():
    return 0


def count_by_race():
    racecount = defaultdict(int)
    for inmate in get_inmate_data():
        racecount[inmate['race']] += 1
    return racecount


def count_young_offenders_by_race():
    racecount = {}
    for inmate in get_inmate_data():
        if inmate['age_at_offense'] <= 21:
            rtype = inmate['race']
            if racecount.get(rtype):
                racecount[rtype] += 1
            else:
                racecount[rtype] = 1
    return racecount


def count_by_race_within_age_at_offence(min_age=-1, max_age=999):
    racecount = {}
    for inmate in get_inmate_data():
        _age = inmate['age_at_offense']
        if _age >= min_age and _age <= max_age:
            rtype = inmate['race']
            if racecount.get(rtype):
                racecount[rtype] += 1
            else:
                racecount[rtype] = 1
    return racecount
