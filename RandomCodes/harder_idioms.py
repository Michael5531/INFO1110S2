import sys
a = input("Enter some integers: ")
split = a.split(', ')
new = []
i = 0
while i < len(split):
    new.append(int(split[i]))
    i += 1
print("Your integers were: {}".format(new))
if sys.argv[1] == "-find8":
    found8 = False
    j = 0
    while j < len(new):
        if new[j] == 8:
            found8 == True
            print("The number 8 is at index {}.".format(j))
            break
        else:
            print("The number 8 is at index -1.")
            break
        j += 1
halve = []
if sys.argv[1] == "-evens":
    i = 0
    while i < len(new):
        if new[i] % 2 != 0:
            halve.append(int(new[i]))
        if new[i] % 2 == 0:
            halve.append(int(new[i] / 2))
        i += 1
    print("Halve even numbers: {}".format(halve))
factors = []
if sys.argv[1] == "-factor8":
    k = 0 
    while k < len(new):
        if new[k] % 8 == 0:
            factors.append(new[k])
        k += 1
    print("Multiples of 8 are {}".format(factors))

