"""This is the entry point of the program."""


def highest_number_cubed(limit):
    if isinstance(limit, float):
        return 'please insert an integer'
    else:
        floater = limit**(1./3)
        return int(floater)
