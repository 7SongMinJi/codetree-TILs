given_str = input()

for i in range(len(given_str), -1, -1):
    if i % 2 == 1:
        print(given_str[i], end="")