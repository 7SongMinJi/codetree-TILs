given_str = input()

L = len(given_str)
print(given_str)

for _ in range(L):
    given_str = given_str[-1] + given_str[:-1]
    print(given_str)