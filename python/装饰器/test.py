# 方法一和方法二的作用是一致的
# 打印如下：
# Before function call
# Hello!
# After function call

# 方法一 start
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()  # 调用原函数
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 方法一 end

# 方法二 start
def my_decorator1(func):
    print("Before function call")
    func()  # 调用原函数
    print("After function call")

def say_hello1():
    print("Hello!")

my_decorator1(say_hello1)
# 方法二 end
