def CtoF(Cdegrees):
	""" Converts list of Celsius values to Farenheit.  Prints a table of celsius values on the left,
	and the farenheit conversion on the right.
>>> CtoF([-2,4,5,6,6])
   -2  28.4
    4  39.2
    5  41.0
    6  42.8
    6  42.8
>>> x = [-1,-2,-3,-4,10,20,30,40]
>>> CtoF(x)
   -1  30.2
   -2  28.4
   -3  26.6
   -4  24.8
   10  50.0
   20  68.0
   30  86.0
   40 104.0
>>> tuplelist = ([-5,-2,-1],[4,1,-4,3,-3,0],[2,2,2,2,2,2])
>>> CtoF(tuplelist[1])
    4  39.2
    1  33.8
   -4  24.8
    3  37.4
   -3  26.6
    0  32.0
>>> CtoF(tuplelist[0])
   -5  23.0
   -2  28.4
   -1  30.2
>>> CtoF(tuplelist[2])
    2  35.6
    2  35.6
    2  35.6
    2  35.6
    2  35.6
    2  35.6
	"""
	for C in Cdegrees:
		F = (9.0/5)*C + 32.
		print '%5d %5.1f' % (C, F)
	
#C = [-20, -15, -5, 5, 10, 15, 20]
#CtoF(C)

if __name__ == "__main__":
	import doctest
	doctest.testmod()