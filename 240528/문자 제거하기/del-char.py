string = input()
arr = list(string)

while True:
    x = int(input())
    if len(arr) <= x:
        arr.pop(len(arr) - 1)
    else:
        arr.pop(x)
    print(''.join(arr))
    if len(arr) == 1:
        break

# // 처음에 틀렸는데 그 이유가 string 문자열일 경우 pop 할 수 없기 때문 ***
# 그래서 string을 list로 바꾼 다음 pop해줘야 함!! ***