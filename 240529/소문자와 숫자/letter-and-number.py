given_str = input()

for elem in given_str:
    if elem.isalpha() == True or elem.isdigit() == True:
        if ord(elem) >= ord('A') and ord(elem) <= ord('Z'):
            print(elem.lower(), end="")
        else:
            print(elem, end="")