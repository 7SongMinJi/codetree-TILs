# 입력을 몇 번 받을지 모르겠을 땐 while True: 무한루프를 이용하자! & if-break문 활용
while True:
    n = int(input())
    if n < 25:
        print("Higher")
    elif n > 25:
        print("Lower")
    else:
        print("Good")
        break