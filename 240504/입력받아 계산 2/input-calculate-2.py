# # 파이썬 - 한 줄 단위로 input 입력 받음
# a = input() # 3 2 입력
# print(a) # 3 2 출력

# # split() 함수 이용 - 공백(default)을 기준으로 ***문자열(['3', '2']와 같은 형태)***이 잘라져 list가 만들어짐
# print(a.split()) # ['3', '2'] 출력

# # list란: 여러 원소의 묶음. list 안에 있는 각 원소를 참조하기 위해서는 [] 이용 & index는 0부터 시작

# arr = [5, 6, 10]
# print(f"First element is {arr[0]}")
# print(f"Second element is {arr[1]}")
# print(f"Third element is {arr[2]}")

# 공백을 사이에 두고 두 정수를 입력받아 각각의 정수를 변수 n, m에 순서대로 넣어주기
# 대신!! 문자열의 형태로 split 된다는 것!! 주의~!
# a = input()
# arr = a.split()
# n = arr[0]
# m = arr[1]

# print(n)
# print(m)
# print(n * m)
# // 이렇게 하면 오류

# a = input()
# arr = a.split()
# n = int(arr[0])
# m = int(arr[1])

# print(n)
# print(m)
# print(n * m)

# # input()과 split() 코드 한줄에 작성하기
# arr = input().split()
# n = int(arr[0])
# m = int(arr[1])

# print(n)
# print(m)
# print(n * m)

# arr = int(input().split()) # 이건 안 되나봐


# 문제
x = input().split()

a = int(x[0])
b = int(x[1])

print(a * b)