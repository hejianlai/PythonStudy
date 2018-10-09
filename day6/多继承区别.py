__author__ = "Alex Li"

class A:
    def __init__(self):
        print("A")
class B(A):
    pass
    # def __init__(self):
    #     print("B")
class C(A):
    pass
    # def __init__(self):
    #     print("C")
class D(B,C):
    pass
    # def __init__(self):
    #     print("D")


obj = D()
#python2的经典类是按深度优先来继承的 ，新式类是按广度优先来进行的
#python3的经典类和新式类都是统一按广度优先来继承的