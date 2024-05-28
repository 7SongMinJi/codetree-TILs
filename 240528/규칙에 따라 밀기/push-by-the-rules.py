strA = input()
command = list(input())

for elem in command:
    if elem == 'L':
        strA = strA[1:] + strA[0]
    elif elem == 'R':
        strA = strA[-1] + strA[:-1]

print(strA)

# // 처음에 틀렸는데 그 이유가 input().split()은 공백을 기준으로 나눠서 list를 만드는 것
# // 하나의 문자열을 각 문자로 쪼개어 list를 만들려면 list(input()) 해야 함!