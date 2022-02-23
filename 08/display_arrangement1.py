from seating import Seating

def display_arrangement(seatings, time):
    print("Seatings Arrangement for " + time + ":")
    
    for i in range(len(seatings)):
        if (seatings[i].is_free):
            print("o ", end='')
        else:
            print("x ", end='')
    
    print()