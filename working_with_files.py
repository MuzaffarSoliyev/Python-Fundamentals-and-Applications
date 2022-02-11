import os

print(os.getcwd())
print(os.listdir('.idea'))

for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)