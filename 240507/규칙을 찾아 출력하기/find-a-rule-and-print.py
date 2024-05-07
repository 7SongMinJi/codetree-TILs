n = int(input())

for i in range(n):
    for j in range(n):
        if i != 0 and i != (n-1) and j != 0 and j != (n-1) and i <= j:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()


# # 정답 코드

# # 변수 선언 및 입력
# n = int(input())
	
# # n칸의 정사각형에서 i, j가 조건에 맞으면 *을 출력합니다.
# for i in range(n):
# 	for j in range(n):
# 		if i > j or i == 0 or j == n - 1:
# 			print("* ", end="")
# 		else:
# 			print("  ", end="")
# 	print()