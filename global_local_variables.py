x = 1
y = 2
z = 3


def function1(x:int)->int:
    x = x * 10
    return x


def function2(result:int)->int:
    result -= x
    return result


def function3()->int:
    global y
    y += 5
    return y


//What do you think the expected values will be?
print(function1(z))
print(function2(10))
print(function3())
