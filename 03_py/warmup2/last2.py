def last2(s):
    if len(s) < 2:
        return 0
    last_2_chars = s[-2:]
    count = 0
    for i in range(len(s) - 2):
        if s[i:i+2] == last_2_chars:
            count += 1
    return count