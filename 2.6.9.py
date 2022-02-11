matrix = []

while True:
    row = input()
    if row != 'end':
        row = list(map(int, row.split()))
        matrix.append(row)
    else:
        break


n = len(matrix)
m = len(matrix[0])

matrix_1 = []
for i in range(n):
    matrix_1.append([''] * m)

for i in range(n):
    for j in range(m):
        idx_1 = n - 1 if i - 1 < 0 else i - 1
        idx_2 = 0 if i + 1 > n - 1 else i + 1
        idx_3 = m - 1 if j - 1 < 0 else j - 1
        idx_4 = 0 if j + 1 > m - 1 else j + 1

        matrix_1[i][j] = str(matrix[idx_1][j] + matrix[idx_2][j] + matrix[i][idx_3] + matrix[i][idx_4])

for i in matrix_1:
    print(' '.join(i))