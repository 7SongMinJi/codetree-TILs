# arr = list()

# n = int(input())

# while n != 0:
#     arr.append(n)
#     n = int(input())

# for elem in arr[::-1]:
#     print(elem, end=" ")

# // 하나씩 입력받는 경우에만 이렇게 짤 수 있는 거. 문제에선 한 줄로 쭉 주어지는 거니까 이렇게 짜면 안 됨!

# arr = list(map(int, input().split()))

# for elem in arr:
#     if elem == 0:
#         arr.pop()
#         break

# for elem in arr[::-1]:
#     print(elem, end=" ")

# // 중간에 0이 있고 그 뒤로도 있는 경우 이렇게 하면 틀림!!

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        i -= 1
        break

for elem in arr[i::-1]:
    print(elem, end=" ")