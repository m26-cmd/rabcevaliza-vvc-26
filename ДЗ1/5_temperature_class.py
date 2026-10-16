class temperature_converter:
    def c_v_k(self):
        return self.t + 273
    def k_v_c(self):
        return self.t - 273

print("1: Цельсия -> Кельвина")
print("2: Кельвина -> Цельсия")
c = int(input("Выбери 1 или 2: ")) 
t = int(input("Введи значение температуры: "))

conv = temperature_converter()
conv.t = t
if c == 1:
    print("Температура:",conv.c_v_k(), "К")
elif c == 2:
    print("Температура:", conv.k_v_c(), "℃")
else: 
    print("Error")    
