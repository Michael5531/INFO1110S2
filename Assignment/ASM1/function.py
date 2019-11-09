def process_file(filename):
    import sys
    bank_value = []
    try:
        f = open(filename, "r")
        line = f.readlines()
        f.close()
    except FileNotFoundError or FileExistsError or EOFError:
        raise ValueError("Error: String does not represent a valid file!")
        quit()
    i = 0
    while i < len(line):
        a = line[i].split("\n")
        value_in_use = float(str(a[0]))
        bank_value.append(value_in_use)
        i += 1
    j = 0
    income_list = []
    expense_list = []
    while j < len(bank_value):
        if j % 2 == 0:
            income_list.append(bank_value[j])
        else:
            expense_list.append(bank_value[j])
        j += 1
    return (income_list, expense_list)
#([5.0, 3.0, 7.35, 0.0, 14.9, 6.0, 6.0], [4.0, 2.0, 1.0, 0.0, 5.0, 3.0, 5.0])
#Income first, Expense after