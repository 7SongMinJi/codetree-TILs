# # List - 한 줄에 공백을 사이에 두고 10개의 숫자가 주어졌을 때, 이 숫자들의 합을 구하기

# # // 지금까지... 공백을 사이에 두고 숫자가 주어지는 경우 input().split()으로 입력받을 수 있음
# arr = input().split()
# print(arr)
# sum_val = int(arr[0]) + int(arr[1]) + ... + int(arr[9])
# print(sum_val)
# # 3 5 7 -> ['3', '5', '7']
# # => 각 원소의 type은 string!!!

# # 그치만 위의 코드를 for문을 이용해 출력하면 더 쉬울 것!
# # => 0부터 10 전까지 arr를 순회하며 합을 구하기

# arr = input().split()
# sum_val = 0
# for i in range(10):
#     sum_val += int(arr[i])
# print(sum_val)


# # list에 있는 원소를 순차적으로 탐색하는 코드
# # elem 위치에 arr 안에 있는 원소들이 순차적으로 하나씩 들어가게 됨 *****

# arr = [1, 2]
# for elem in arr:
#     print(elem)


# # 10개의 숫자를 한 줄에 공백을 사이에 두고 입력받는 경우, list로 변환하였을 때 원소의 type이 문자열임
# # 일일이 int()로 type을 변환해줘야 해서 번거로움
# # => map()이라는 함수를 이용하면 편하게 가능!
# # map() 함수: 리스트에 있는 원소 type을 전부 변환한 이후의 리스트를 반환해줌

# arr = list(map(int, input().split()))
# print(arr)

# # 한 줄에 n, m 2개의 숫자를 공백을 사이에 두고 입력 받는 경우에 tuple과 map을 이용하면 됨!
# # ***** tuple로 map 함수를 감싸면, n, m에 각 숫자를 나눠 할당해 줄 수 있음 *****
# n, m = tuple(list(map(int, input().split())))
# print(n, m)


# 문제
arr = list(map(int, input().split()))
sum_val = 0

for i in range(10):
    sum_val += arr[i]

print(sum_val)