import os

os.chdir('main')

answers = []

for current_dir, dirs, files in os.walk('.'):
    # print(current_dir, dirs, files)
    for file in files:
        if file.split('.')[1] == 'py':
            answers.append(current_dir.replace('\\', '/').replace('.', '')[1:])
            break

# print(answers)
with open('../out.txt', 'w') as f:
    f.write('\n'.join(answers))
