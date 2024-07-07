# 최대공약수 구하기

# n, m이 주어졌을 때, n과 m의 최대공약수를 출력하는 프로그램 작성하기

n, m = tuple(map(int, input().split()))

def print_common_divisor(n, m):
    while m:
        n, m = m, n % m
    print(n)

print_common_divisor(n, m)