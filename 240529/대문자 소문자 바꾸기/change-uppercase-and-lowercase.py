given_str = input()

for elem in given_str:
    if elem >= 'A' and elem <= 'Z':
        print(elem.lower(), end="")
    elif elem >= 'a' and elem <= 'z':
        print(elem.upper(), end="")