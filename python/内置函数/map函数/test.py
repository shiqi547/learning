def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # 输出: [1, 4, 9, 16]
print(squared_numbers)        # 输出: <map object at 0x0000021107819E10>