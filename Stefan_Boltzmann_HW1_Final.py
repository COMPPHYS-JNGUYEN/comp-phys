from math import e, pi

def f(y):                                   #Integrand
    return (y**3)/(e**y - 1)

def fractionaldifference(prev, curr):       #Calculates the fractional difference between the current answer for integral and previous.
    frac_diff = (curr - prev)/float(curr)
    return frac_diff

def integral(intial, final, steps, dy):     #Used to find integral when given the starting and ending points, desired starting number of steps, and how wide the step should be.
    frac_diff = 1                           #Needed to initialize frac_diff to start while loop, then reassigned frac_diff by calling fractionaldifference().
    integral_previous = 0.                  #Initialize integral_previous.
    print 'running...'
    while frac_diff > 1e-6:                 #After frac_diff reaches 1e-6, stop while loop.
        integral_current = 0.               #Initialize integral_current.
        for y in range(1, int(steps + 1)):  #Use of for loop to evaluate bounds of integral with range, plugging in values, y.
            height = f(y * dy)              #Using rectangular method of integral approximation, calculate height of rectangle.
            area = dy * height              #Area of rectangle.
            integral_current += area        #Need to update integral_current so it outputs.
        frac_diff = fractionaldifference(integral_previous, integral_current)
        if frac_diff == 1.0:                #Used to determine if the integral_current has anything to be compared to.  If it's the first frac_diff, then there will be no integral_previous to copmpare integral_current to.
            print 'number of steps:{:4} \ndy = {:1.4f}, integral = {:1.7f} \nfrac_diff = N/A\n'.format(int(steps), dy, integral_current, 100*frac_diff)
            integral_previous = integral_current
            steps *= 2.                     #Update steps such that the number of steps doubles, steps meaning rectangles.  The more rectangles, the better the approximation.
            dy /= 2.                        #Update dy such that it becomes smaller and smaller.  The smaller dy is and the more rectangles under the curve, the better the approximation.
        else:
            print 'number of steps:{:4} \ndy = {:1.4f}, integral = {:1.7f} \nfrac_diff = {:1.7f}%\n'.format(int(steps), dy, integral_current, 100*frac_diff)
            integral_previous = integral_current
            steps *= 2.                     #Update steps such that the number of steps doubles, steps meaning rectangles.  The more rectangles, the better the approximation.
            dy /= 2.                        #Update dy such that it becomes smaller and smaller.  The smaller dy is and the more rectangles under the curve, the better the approximation.
    answer = (pi**4)/15.                    #Full solution to integral.  Used to compare coded answer to complete answer.
    fractional_error = 100*(answer - integral_previous)/answer     #Fractional error between actual answer and answer from coded integral.
    print 'The integral evaluated to within specified accuracy: {:}'.format(integral_current)
    print 'The upper limit of its fractional error is estimated to be: {:}'.format(frac_diff)
    print 'The correct answer is: {:}'.format(answer)
    print 'The actual fractional error is: {:}%\n'.format(fractional_error)
    return integral_previous                #Return integral_previous because after while loop is finished, at end of for loop, integral_current is assigned to integral_previous.

test = integral(0, 100, 100, 1)             #Confirmation that code works.  Can be used for various other values of initial, final, steps, and dy, although steps seems to have a maximum of 709 (error at 710).
test2 = integral(50, 120, 100, 5)
test3 = integral(0,345, 3, 3)
