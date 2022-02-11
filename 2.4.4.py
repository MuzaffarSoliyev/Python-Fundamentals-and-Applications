with open('in.txt', 'r') as f:
    text = f.read().split('\n')

text.reverse()

with open('out.txt', 'w') as f:
    f.write('\n'.join(text))
