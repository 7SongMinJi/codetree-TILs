n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

print(arr[0], arr[1])

# // 위에서 나온 파이썬 문법 제대로 알고 있기
# 정렬할 때 arr = arr.sort() 이렇게 다시 저장해줄 필요 없고!! 그냥 arr.sort()
# arr.sort() - 오름차순이 default, 내림차순 원할 경우 arr.sort(reverse=True)