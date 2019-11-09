def starts_wtih(word, chs):
    start = word[0]
    is_found = False
    i = 0
    while i < len(chs):
        if chs[i] == start:
            is_found = True
        i += 1
    return is_found

def search(words, starts_chs):
    tmp = []
    i = 0
    while i < len(words):
        if len(words[i]) == 0:
            i += 1
            continue
        tmp.append(words[i][0])
        i += 1
    return tmp
words = ['frosty', 'chocolate', 'milkshake', '', 'glazed', 'raspberry', 'donut']
start_chs = ['a', 'b', 'c', 'd']
filtered_words = search(words, start_chs)
print(filtered_words)
