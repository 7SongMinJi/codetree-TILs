arr = input().split()

h, w = int(arr[0]), int(arr[1])

b = 10000 * w / (h**2)

print("%d" % b)
# 참고로 %d일 땐 버림, %.1f 이런 건 반올림

if b >= 25:
    print("Obesity")