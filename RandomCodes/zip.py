def my_zip(a_ls, b_ls):
    if len(a_ls) == len(b_ls):
        tmp = []
        i = 0
        while i < len(a_ls):
            tmp.append((a_ls[i],b_ls[i]))
            i += 1
    return tmp
a_spam = ['a', 'b', 'c', 'd']
b_spam = ['W', 'X', 'Y', 'Z']
z_spam = my_zip(a_spam, b_spam)
print(z_spam)

