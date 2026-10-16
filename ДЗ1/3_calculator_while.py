def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def umnojenie(a,b):
    return a*b
def delenie(a,b):
    return a/b
    
while True:                
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = input("Введите любую операцию (*, +, -, /): ")
    if c == "+":
	    print(plus(a,b))
    elif c == "-":
	    print(minus(a,b))
    elif c == "*":
	    print(umnojenie(a,b))
    elif c == "/":
        if b == 0:
            print("Error")
        else:
	        print(delenie(a,b))
    else:
	    print("Error")