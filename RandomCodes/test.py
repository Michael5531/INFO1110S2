import sys
try:
    f = open(sys.argv[1], "r")
    file = f.reareadlines()
    f.close()
except IndexError:    
    print("There's no file for this")