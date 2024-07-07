# 최소공배수 구하기

n, m = tuple(map(int, input().split()))

def print_lcm(n, m):
    def gcd(n, m):
        while m:
            n, m = m, n % m
        return n
    
    def lcm(n, m):
        return n * m // gcd(n, m)
    
    print(lcm(n, m))

print_lcm(n, m)