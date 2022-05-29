def addBinary(a, b) -> str:
    x, y = int(a, 2), int(b, 2)
    print(f"initial x, y: {x}, {y}")
    while y:
        print(f"curr y: {y}")
        x, y = x ^ y, (x & y) << 1
        print(f"x: {x}, y: {y}")
    print(f"result: {bin(x)[2:]}")      
    return bin(x)[2:]

a = '1111'
b = '0010'

addBinary(a,b)
