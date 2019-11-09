import sys
store = []
while True:
    a = input("Number: ")
    if a != "0":
        store.append(a)
    if a == "0":
        print("Your numbers were: ")
        break
if sys.argv[1] == "-sum":
    i = 0
    sum = 0
    while i < len(store):
        sum += float(store[i])
        print(store[i])
        i += 1
    print('The sum of those number is {}'.format(sum))
if sys.argv[1] == "-avg":
    i = 0
    count = 0
    sum = 0
    while i < len(store):
        sum += float(store[i])
        count += 1
        avg = sum / count
        print(store[i])
        i += 1
    print("The average of those number is {}".format(avg))
if sys.argv[1] == "-max":
    i = 0
    max = float(store[0])
    while i < len(store):
        if float(store[i]) > max:
            max = float(store[i])
        print(store[i])
        i += 1
    print('The largest number is {}'.format(max))
if sys.argv[1] == "-min":
    i = 0 
    min = float(store[0])
    while i < len(store):
        if float(store[i]) < min:
            min = store[i]
        print(store[i])
        i += 1
    print("The smallest number is {}".format(min))


