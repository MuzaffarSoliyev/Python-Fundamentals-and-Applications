import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'human', r'computer', line)
    print(line)
