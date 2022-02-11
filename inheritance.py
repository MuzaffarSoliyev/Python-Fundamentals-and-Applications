class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(B, C, D):
    pass

# E().foo()
# print(E().foo())
print(E().mro())