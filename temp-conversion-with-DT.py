""" Converts list of Celsius values to Farenheit.  Prints a table of celsius values on the left,
	and the farenheit conversion on the right.
    >>> CtoF(5)
    41.0
"""

def CtoF(Cdegrees):
    F = (9.0/5)*Cdegrees + 32.
    return F


if __name__ == "__main__":
    import doctest
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-Cdegrees', type = float)
    args = parser.parse_args()
    Cdegrees = args.Cdegrees
    y = CtoF(Cdegrees)
    print y
