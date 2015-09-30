import pprint as pp

class Airline:
    def __init__(self, flight):
        self.flight = flight
        
    def SortbyAirline(self):
        data = sorted(self.flight, key = lambda airline:airline[0:2])
        return data

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


X = []
Y = []
Z = []
U = []
V = []

[X.append(flights[i][0]) for i in range(len(flights))]                                   # Appends index1-th element of i-th element of data to empty list X with list comprehension.
[Y.append(flights[i][1]) for i in range(len(flights))]
[Z.append(flights[i][2]) for i in range(len(flights))]                                   # Appends index1-th element of i-th element of data to empty list X with list comprehension.
[U.append(flights[i][3]) for i in range(len(flights))]  
[V.append(flights[i][4]) for i in range(len(flights))]

cool = zip(X, Y, Z, U, V)
print 'Flight\tDestination\tGate\tTime\n\
--------------------------------------------------'
for A, B, C, D, E in cool:
    print '{:9s} {:4d}\t{:3s}\t{:2d}\t{:f}'.format(A, B, C, D, E)