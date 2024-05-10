count_arr = [0] * 4

for i in range(3):
    arr = input().split()
    cold = arr[0]
    temp = int(arr[1])
    if cold == 'Y' and temp >= 37:
        count_arr[0] += 1
    elif cold == 'N' and temp >= 37:
        count_arr[1] += 1
    elif cold == 'Y' and temp < 37:
        count_arr[2] += 1
    else:
        count_arr[3] += 1

for elem in count_arr:
    print(elem, end=" ")
if count_arr[0] >= 2:
    print("E")