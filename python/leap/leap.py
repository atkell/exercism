def is_leap_year(year):
    # we may use the modulous here to check if there is any remainder
    if year % 4 != 0:
        return False
    elif ((year % 4 == 0) and (year % 100 == 0)) and (year % 400 != 0):
        return False
    else:
        return True


