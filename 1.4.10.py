GLOBAL_NAMESPACES = {
    'global': {
        'parent': None,
        'vars': []
    }
}


def create(n, v):
    global GLOBAL_NAMESPACES
    GLOBAL_NAMESPACES[n] = {'parent': v, 'vars': []}


def add(n, v):
    global GLOBAL_NAMESPACES
    GLOBAL_NAMESPACES[n]['vars'].append(v)


def get(n, v):
    global GLOBAL_NAMESPACES
    if v in GLOBAL_NAMESPACES[n]['vars']:
        return n
    elif n == 'global':
        return None
    else:
        return get(GLOBAL_NAMESPACES[n]['parent'], v)


n = int(input())

for i in range(n):
    command, namespace, value = input().split()
    if command == 'create':
        create(namespace, value)
    elif command == 'add':
        add(namespace, value)
    elif command == 'get':
        print(get(namespace, value))
