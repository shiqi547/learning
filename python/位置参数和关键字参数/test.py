def bar1(*args, **kwargs):
    print(args)
    for arg in args:
        print(arg)
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

bar1(1, 2, 3, 4, name="Alice", age=30, city="New York", key="value")

### 打印如下：

# (1, 2, 3, 4)
# 1
# 2
# 3
# 4
# {'name': 'Alice', 'age': 30, 'city': 'New York', 'key': 'value'}
# name: Alice
# age: 30
# city: New York
# key: value