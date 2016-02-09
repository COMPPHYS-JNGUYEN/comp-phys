'''
To run tests: 

	> py.test intro_pytest.py

Verbose (-v): 

	> py.test -v intro_pytest.py
       
'''



def multiplication(x, y):
    return x*y
#    return x*y + 1


def test_multiplication():
    assert multiplication(5, 4) == 20
	
