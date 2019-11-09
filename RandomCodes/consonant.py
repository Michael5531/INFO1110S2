def consonant(ch):
    if len(ch) > 1:
        return False
    elif ch == "a" or "e" or "i" or "o" or "u":
        return True
    else:
        return False
ch = "a"
consonant(ch)
