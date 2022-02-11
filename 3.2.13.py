import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'\b[Aa]+\b', r'argh', line, 1)
    print(line)