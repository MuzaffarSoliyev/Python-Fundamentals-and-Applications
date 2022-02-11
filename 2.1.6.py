try:
    foo()
except AssertionError:
    print("AssertionError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")

print(AssertionError.mro())
