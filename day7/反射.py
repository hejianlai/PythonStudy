__author__ = "Alex Li"

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)


d = Dog("NiuHanYang")
choice = input(">>:").strip()

if hasattr(d,choice):
    getattr(d,choice)
else:
    setattr(d,choice,bulk) #d.talk = bulk
    func = getattr(d, choice)
    func(d)

#hasattr(obj,name_str) 判断一个对象里是否有对应的name_str字符串的方法
#getattr(obj,name_str) 根据字符串去获取obj对象里的对应的方法的内存地址
#setattr(obj，'y',z) is equivalent to 
#delattr(obj,name_str) 删除一个属性
