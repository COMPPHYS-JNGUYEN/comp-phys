## Cleaner version of first and fourth cells
## Need to figure out how to put lists into column/table form

import pprint

def sortXvsY(data, index1=0, index2=0):
	"""
		Function takes data and sorts the data according to which indices are desired.  For example, in the variable data2 below are data pertaining to star names, distance from the Sun
		in light years, apparent brightness according to how bright it is in our sky compared to Sirius A, and absolute brightness-- how bright the stars would look if all were the same
		distance as the Sun, compared with the Sun.  The program takes the data, and sorts it alphabetically if desired by name.  If distance is desired, indicate the corresponding indices
		and the program will sort the data according to Name vs. (Desired), e.g. Name vs. Apparent Brightness.

>>> sortXvsY(data2)
Sorted data according to index 0.
<BLANKLINE>
[('Alpha Centauri A', 4.3, 0.26, 1.56),
 ('Alpha Centauri B', 4.3, 0.077, 0.45),
 ('Alpha Centauri C', 4.2, 1e-05, 6e-05),
 ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
 ("Barnard's Star", 6.0, 4e-05, 0.0005),
 ('Luyten 726-8 A', 8.4, 3e-06, 6e-05),
 ('Luyten 726-8 B', 8.4, 2e-06, 4e-05),
 ('Ross 154', 9.4, 2e-05, 0.0005),
 ('Sirius A', 8.6, 1.0, 23.6),
 ('Sirius B', 8.6, 0.001, 0.003),
 ('Wolf 359', 7.7, 1e-06, 2e-05)]
<BLANKLINE>
>>> sortXvsY(data2, 4, 1)
Cannot use provided indices.  Max index is 3.
	"""
	if index1 or index2 >= len(data[0]):		# Wanted to generalize function given different data, but same format.  If either index is out of range, print message and stop remainder of program.
		LenDataElement = len(data[0])			# Length of element in data, used to establish how high index can go.
		print 'Cannot use provided indices.  Max index is {}.'.format(LenDataElement - 1)	# Prints out error message, stating that index maxes out at len(data[0]).
		return									# Exits out of function
	elif index1 == index2:						# If indices equal to each other after passing first (if) condition, then sort data according to index2 (although using either index doesn't matter since both are equal).						
		print 'Sorted data according to index {}.\n'.format(index2)							# A notice to user that because indices matched, sorted data by default indices or equal indices.
		x = pprint.pprint(sorted(data, key = lambda x: x[index2]))								# Sort data, and pretty print, according to index2.
		print									# Empty line to make printing look nicer.
		return x
   
	data = sorted(data, key = lambda x: x[index2])											# Sort data according to given index, index2.
	X = []										# Empty list for first desired list, used for initialization.
	Y = []										# Empty list for second desired list, used for initialization.
	[X.append(data[i][index1]) for i in range(len(data))]									# Appends index1-th element of i-th element of data to empty list X with list comprehension.
	[Y.append(data[i][index2]) for i in range(len(data))]									# Appends index1-th element of i-th element of data to empty list Y with list comprehension.
	if index2 == 0:								# This if statement and following statements added mainly for the sake of the homework.  We know that the 0 through 3 indices correspond to name, distance, apparent brightness, and absolute brightness respectively.
		print 'Ranked by Name:'
	elif index2 == 1:
		print 'Ranked by Distance:\n'
	elif index2 == 2:
		print 'Ranked by Apparent Brightness:\n'
	elif index2 == 3:
		print 'Ranked by Absolute Brightness:\n'
	else:
		print 'Ranked by {:}:\n'.format(index2)	# Used when using unspecified data set, as opposed to our given data, with regards to particular index, but same formatting as given data set.
	table = [X] + [Y]							# Concatenates [X] and [Y] together to make table of two desired lists.
	pprint.pprint(table)						# Nicely prints out table.
	#pprint.pprint(X), pprint.pprint(Y)			# Nicely prints out lists X and Y.
	print										# Adds empty line
    

data2 = [
('Alpha Centauri A',    4.3,    0.26,       1.56),
('Alpha Centauri B',    4.3,    0.077,      0.45),
('Alpha Centauri C',    4.2,    0.00001,    0.00006),
("Barnard's Star",      6.0,    0.00004,    0.0005),
('Wolf 359',            7.7,    0.000001,   0.00002),
('BD +36 degrees 2147', 8.2,    0.0003,     0.006),
('Luyten 726-8 A',      8.4,    0.000003,   0.00006),
('Luyten 726-8 B',      8.4,    0.000002,   0.00004),
('Sirius A',            8.6,    1.00,       23.6),
('Sirius B',            8.6,    0.001,      0.003),
('Ross 154',            9.4,    0.00002,    0.0005),
]

sortXvsY(data2, 0, 1)
#sortXvsY(data2, 0, 2)
#sortXvsY(data2, 0, 3)


if __name__ == "__main__":
	import doctest
	doctest.testmod()