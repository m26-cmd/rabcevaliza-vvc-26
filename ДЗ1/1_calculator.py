a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите любую операцию (*, +, -, /): ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b == 0:
        print("Error")
    else:
        print(a / b)
else:
    print("Error")
