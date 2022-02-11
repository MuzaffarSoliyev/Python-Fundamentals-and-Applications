num = input()

idx = 0
sum_1 = 0
sum_2 = 0
for i in num:
    if idx < 3:
        sum_1 += int(i)
    else:
        sum_2 += int(i)
    idx += 1
if sum_1 == sum_2:
    print('Счастливый')
else:
    print('Обычный')
    