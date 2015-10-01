import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-C', type = float)
args = parser.parse_args()

i = True
while i:
    try:
    # if C is not entered at the command line, args.C will be of type None
        args.C/2.
    # would this catch the error?
    # print C
    except:
        print '\nYou failed to provide Celsius degrees as input on the command line!\n'
        C = raw_input("Please enter another temperature: ")
    else:
        C = args.C

    try:
        float(C)
    except:
        YorN = raw_input("Would you like to terminate? (Y/N)")
        if YorN == 'Y' or YorN == 'y':
            exit(1)
    else:
        i = False

F = 9.*float(C)/5. + 32.
print F