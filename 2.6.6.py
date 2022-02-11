numbers = []
sum = 0
squares = 0
while True:
    num = int(input())
    sum += num
    squares += num * num
    if sum == 0:
        break
print(squares)