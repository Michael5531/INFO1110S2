def process_file(filename):
    import sys
    try:
        f = open(sys.argv[1], "r")
        file_use = f.readlines()
        f.close()
    except FileExistsError:
        raise ValueError('Error: String does not represent a valid file!')
        sys.exit()
    list_incomes=[]
    list_expenses = []
    num = []
    for index in file_use:
        num.append(index.rstrip())
    i = 0
    while i <len(num):
        if i %2 == 0:
            list_incomes.append(float(num[i]))
        else:
            list_expenses.append(float(num[i]))
        i += 1
    week = (list_incomes, list_expenses)
    return week