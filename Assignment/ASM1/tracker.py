import sys
from function import process_file


weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Write your code here
#+---------------------------EXCEPTIONS-------------------------+
day = 0
if len(sys.argv) < 2:
    print("Error: Not enough command line arguments!")
    exit()
try:
    f = process_file(sys.argv[1])
    a = open(sys.argv[1],'r')
except ValueError:
    print("Error: File not found!")
    quit()
try:
    start_balance = float(input("Starting balance: $"))
except ValueError:
    print("Error: Cannot convert to float!")
    exit()
current = start_balance + f[0][day] - f[1][day]
if start_balance <= 0:
    print("Error: Must start with positive balance!")
    exit()
#+------------------------------STARTS-----------------------------+
print()
while True:
    f = process_file(sys.argv[1])
    cmd = input("Enter command: ")
#+----------------------------TRANSACTION--------------------------+
    if cmd == "transaction":
        try:
            amout_in = float(input("Enter amount: $"))
            current += amout_in
        except ValueError:
            print("Error: Cannot convert to float!")
            print()
            continue
        print()
#+-----------------------------STATUS-----------------------------+
    elif cmd == "status":
        day_use = day % 7
        day_in_wk = weekdays[day_use]
        print("Day {} ({})".format(int(day), day_in_wk))
        print("Starting balance: ${:.2f}".format(float(start_balance)))
        print("Current balance: ${:.2f}".format(float(current)))
        if float(current) == float(start_balance):
            print()
        elif float(current) > float(start_balance):
            print("Nice work! You're in the black.\n")
        elif float(current) < float(start_balance):
            print("Be careful! You're in the red.\n")
#+------------------------------NEXT-------------------------------+
    elif cmd == "next":
        start_balance = current
        day += 1
        day_use = day % 7
        current = start_balance + f[0][day_use] - f[1][day_use]
        if float(current) < 0:
            print("Oh no! You're in debt!")
            quit()
        else:
            print("Going to the next day...")
            print()
#+----------------------------REGULAR------------------------------+
    elif cmd == "regular":
        file_use = process_file(sys.argv[1])
        print("Regular Transactions:")
        i = 0
        while i < len(file_use[1]):
            print('{}: +${:.2f} -${:.2f}'.format(weekdays[i],file_use[0][i], file_use[1][i]))
            i += 1
        print()
#+------------------------------HELP-------------------------------+
    elif cmd == "help":
        print("The available commands are:")
        print('"transaction": Record a new income or expense')
        print('"next": Move on to the next day')
        print('"status": '+"Show a summary of how you're doing today")
        print('"regular": Show a summary of your regular transactions')
        print('"help": Show this help message')
        print('"quit": Quit the program')
        print()
#+-----------------------------QUIT-------------------------------+
    elif cmd == "quit":
        print("Bye!")
        quit()
#+-----------------------------ELSE--------------------------------+
    else:
        print("Command not found.")
        print('Use the "help" command for a list of available commands')
        print()