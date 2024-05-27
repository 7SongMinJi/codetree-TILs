given_str = input()

ee_cnt, eb_cnt = 0, 0

length = len(given_str)

for i in range(length - 1):
    if given_str[i] == 'e' and given_str[i + 1] == 'e':
        ee_cnt += 1
    elif given_str[i] == 'e' and given_str[i + 1] == 'b':
        eb_cnt += 1

print(ee_cnt, eb_cnt)