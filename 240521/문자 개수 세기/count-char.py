first_input = input()
second_input = input()

cnt = 0

for elem in first_input:
    if elem == second_input:
        cnt += 1

print(cnt)