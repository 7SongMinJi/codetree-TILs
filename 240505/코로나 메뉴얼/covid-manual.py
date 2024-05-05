x_input = input().split()
x_cold, x_temp = x_input[0], int(x_input[1])

y_input = input().split()
y_cold, y_temp = y_input[0], int(y_input[1])

z_input = input().split()
z_cold, z_temp = z_input[0], int(z_input[1])

count = 0

if x_cold == 'Y' and x_temp >= 37:
    x_hosp = 'A'
    count += 1
elif x_cold == 'N' and x_temp >= 37:
    x_hosp = 'B'
elif x_cold == 'Y' and x_temp < 37:
    x_hosp = 'C'
else:
    x_hosp = 'D'

if y_cold == 'Y' and y_temp >= 37:
    y_hosp = 'A'
    count += 1
elif y_cold == 'N' and y_temp >= 37:
    y_hosp = 'B'
elif y_cold == 'Y' and y_temp < 37:
    y_hosp = 'C'
else:
    y_hosp = 'D'

if z_cold == 'Y' and z_temp >= 37:
    z_hosp = 'A'
    count += 1
elif z_cold == 'N' and z_temp >= 37:
    z_hosp = 'B'
elif z_cold == 'Y' and z_temp < 37:
    z_hosp = 'C'
else:
    z_hosp = 'D'

if count >= 2:
    print("E")
else:
    print("N")