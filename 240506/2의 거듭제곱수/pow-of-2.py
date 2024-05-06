n = int(input())

x = 0

while True:
    if n == 1:
        break
    n //= 2
    x += 1

print(x)