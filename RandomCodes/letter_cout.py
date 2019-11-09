def letter_cout(use, string):
    count = 0
    if isinstance(use, (list, tuple)) == False:
        raise TypeError("""‘First input is not a list or a tuple’""")
    i = 0
    while i < len(string):
        if type(string[i]) != str:
            raise InterruptedError("""‘str is not a string!’""")
        else:
            i += 1
            continue
        i += 1
    if type(string) != str:
        raise TypeError("""‘String state str must be a string!’""")
    if string != ("vowels", "consonants"):
        raise ValueError(""""String state str may only be ‘vowels’ or ‘consonants’""")
    else:
        vowels = ("a", "e", "i", "o", "u")
        if string == "vowels":
            i = 0
            while i < len(list):
                j = 0
                while j < len(list[i]):
                    if list[i][j] == vowels:
                        count += 1
                    else:
                        continue
                    j += 1
                i += 1
        elif  string == "consonants":
            z = 0
            while z < len(list):
                p = 0
                while p < len(list[z]):
                    if list[z][p] != vowels:
                        count += 1
                    else:
                        i += 1
                        continue
                    p += 1
                z += 1
        return count
use = ["a", "b", "rer"]
a = letter_cout(use, "vowels")
print(a)