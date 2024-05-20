for i in range(3):
    string_value = input()
    string_len = len(string_value)
    if i == 0:
        max_len = string_len
        min_len = string_len
    else:
        if max_len < string_len:
            max_len = string_len
        if min_len > string_len:
            min_len = string_len

print(max_len - min_len)