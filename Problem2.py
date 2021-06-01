def len_sent(sent):
    sum = 0
    for i in sent:
        sum += 1
    return sum

predl = 'Люблю грозу в начале мая!'
print(len_sent(predl), len(predl))