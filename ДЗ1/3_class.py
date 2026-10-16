class calculator:
    def plus(self):
        return self.a+self.b
    def minus(self):
        return self.a-self.b
    def umnojenie(self):
        return self.a*self.b
    def delenie(self):
        return self.a/self.b
                
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите любую операцию (*, +, -, /): ")
calc = calculator()
calc.a = a
calc.b = b

if c == "+":
	print(calc.plus())
elif c == "-":
	print(calc.minus())
elif c == "*":
	print(calc.umnojenie())
elif c == "/":
    if b == 0:
        print("Error")
    else:
	    print(calc.delenie())
else:
	print("Error")