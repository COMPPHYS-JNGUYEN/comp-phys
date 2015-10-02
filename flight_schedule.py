'''

The program sorts Airport/Airline data given Airline and by time.


'''

import pprint as pp

class Airline:
    def __init__(self, flight):
        self.flight = flight
        
    def SortbyAirline(self):    # Sorts the given data, flight, by Airlines
        data_al = sorted(self.flight, key = lambda airline:airline[0:2])
        X = []
        Y = []
        Z = []
        U = []
        V = []

        [X.append(data_al[i][0]) for i in range(len(data_al))]                                   # Appends index1-th element of i-th element of data to empty list X with list comprehension.
        [Y.append(data_al[i][1]) for i in range(len(data_al))]
        [Z.append(data_al[i][2]) for i in range(len(data_al))]                                 
        [U.append(data_al[i][3]) for i in range(len(data_al))]  
        [V.append(data_al[i][4]) for i in range(len(data_al))]

        cool = zip(X, Y, Z, U, V)
        print 'Flight\t\tDestination\t\tGate\tTime\n-------------------------------------------------------'
        for A, B, C, D, E in cool:      
            print '{:<9s} {:<4d}\t{:<17s}\t{:<2d}\t{:<4.1f}'.format(A, B, airports[C], D, E)
        print
            
    def SortbyTime1(self):      # Sorts the data by Time
        newflights = []
        for tup in self.flight:
            x = list(tup)
            x.insert(0, x[4])   # Inserts time element from data and inserts it into the beginning of the list.
            newflights.append(x)
        newflights2 = sorted(newflights)
        print 'Flight\t\tDestination\t\tGate\tTime\n-------------------------------------------------------'
        for elem in newflights2:
            print '{:<9s} {:<4d}\t{:<17s}\t{:<2d}\t{:<4.1f}'.format(elem[1], elem[2], airports[elem[3]], elem[4], elem[5])
        print
    
    def SortbyTime2(self):  # Sorts the data by Time, but with a lambda function
        data_t = sorted(self.flight, key = lambda time:time[4])
        A = []
        B = []
        C = []
        D = []
        E = []

        [A.append(data_t[i][0]) for i in range(len(data_t))]                                   # Appends index1-th element of i-th element of data to empty list X with list comprehension.
        [B.append(data_t[i][1]) for i in range(len(data_t))]
        [C.append(data_t[i][2]) for i in range(len(data_t))]                                   
        [D.append(data_t[i][3]) for i in range(len(data_t))]  
        [E.append(data_t[i][4]) for i in range(len(data_t))]

        stuff = zip(A, B, C, D, E)
        print 'Flight\t\tDestination\t\tGate\tTime\n-------------------------------------------------------'
        for A, B, C, D, E in stuff:
            print '{:<9s} {:<4d}\t{:<17s}\t{:<2d}\t{:<4.1f}'.format(A, B, airports[C], D, E)
        print
        
airports = \
{"DCA": "Washington, D.C.", "IAD": "Dulles", \
"LHR": "London-Heathrow", "SVO": "Moscow", \
"CDA": "Chicago-Midway", "SBA": "Santa Barbara", \
"LAX": "Los Angeles","JFK": "New York City", \
"MIA": "Miami", "AUM": "Austin, Minnesota"}

# airline, number, heading to, gate, time (decimal hours)
flights = \
[("Southwest",145,"DCA",1,6.00),\
("United",31,"IAD",1,7.1),("United",302,"LHR",5,6.5),\
("Aeroflot",34,"SVO",5,9.00),("Southwest",146,"CDA",1,9.60),\
("United",46,"LAX",5,6.5), ("Southwest",23,"SBA",6,12.5),\
("United",2,"LAX",10,12.5),("Southwest",59,"LAX",11,14.5),\
("American", 1,"JFK",12,11.3),("USAirways", 8,"MIA",20,13.1),\
("United",2032,"MIA",21,15.1),("SpamAir",1,"AUM",42,14.4)]

flight = Airline(flights)
sorted_Airlines = flight.SortbyAirline()
sorted_time = flight.SortbyTime1()
sorted_time2 = flight.SortbyTime2()