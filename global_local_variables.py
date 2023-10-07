x = 1
y = 2
z = 3


def MultiplyTen(x:int)->int:
    x = x * 10
    return x


def Subtract_x(result:int)->int:
    result -= x
    return result


def Add5_to_y()->int:
    global y
    y = 5 + y
    return y



//What do you think the expected outcomes will be?
print(MultiplyTen(z))
print(Subtract_x(10))
print(Add5_to_y())
print(y)
