arr = input().split()

a = int(arr[0])
b = int(arr[1])

if a < b:
    print(1, end=" ")
else:
    print(0, end=" ")

if a == b:
    print(1)
else:
    print(0)

# 위와 같이 파이썬에서 print 함수 사용시 기본적으로 한 줄이 띄워지게 되는데
# 출력 후 뒤에 엔터가 아닌 공백을 출력하고 싶다면 print(값, end=" ") 형태로 작성하기