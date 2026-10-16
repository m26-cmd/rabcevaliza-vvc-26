while True:
    lvl = int(input("Выберите уровень: "))
    if lvl == 1:
        print("Доступные методы:")
        print("Пример: text = прИвЕт_МИР")
        print("upper() - СДЕЛАТЬ ВСЕ БУКВЫ БОЛЬШИМИ. Пример: text.upper() = ПРИВЕТ_МИР")
        print("lower() - сделать все буквы маленькими. Пример: text.lower() = привет_мир")
        print("capitalize() - Сделать только первую букву большой. Пример: text.capitalize() = Привет_мир")
        text = input("Введите текст: ")    
        metod = input("Выберите метод: ")
        if metod == "upper":
            print(text.upper())
        elif metod == "lower":
            print(text.lower())
        elif metod == "capitalize":
            print(text.capitalize())    
        else:
            print("Error")    
    if lvl == 2:
        print("Доступные методы:")
        print("Пример: text = Ботать_это_круто.Очень_круто.")
        print("find() - найти, на каком месте стоит слово (позиция). Пример: text.find() = 11")
        print("replace() - заменить одно слово на другое. Пример: text.replace() = Ботать_это_супер.Очень_супер.")
        print("count() - посчитать, сколько раз слово встречается в тексте. Пример: text.count() = 2 ")
        text = input("Введите текст: ")
        slovo = input("Введите слово, которое нужно найти и зменить: ")
        print("Позиция первого вхождения: ", text.find(slovo))
        slovo1 = input("Введите слово, на которое надо заменить: ")
        new_text = text.replace(slovo, slovo1)
        print("Текст после замены: ", new_text)
        print("Буква 'о' после замены встречается", new_text.count("о"), "раз(а)")
    if lvl == 3:
        print("Доступные методы:")
        print("Пример: text = 1,2,3,4")
        print("split() - разрезать строку на список по разделителю. Пример: text.split =  1 2 3 4 ")
        print("join() - склеить список обратно в строку через разделитель. Пример:  1 2 3 4 -> 1,2,3,4")
        text = input("Введите текст: ")
        metod = input("Выберите метод: ")
        if metod == "split":
            n = input("Введите разделитель: ")
            print(text.split(n))
        elif metod == "join":
            k = input("Введите разделитель: ")
            text1 = text.split(k)    
            n = input("Введите соединитель: ")
            print(n.join(text1))
        else:
            print("Error")        
    if lvl == 4:
        print("Доступные методы:")
        print("Пример: text_4a = '1234*%^$'; text_4b = '___abc1234___' ")
        print("isdigit() - проверить, состоит ли строка ТОЛЬКО из цифр. Пример: text_4a.isdigit() = False")
        print("isalpha() - проверить, состоит ли строка ТОЛЬКО из букв. Пример: text_4a.isalpha() = False")
        print("strip() - убрать лишние символы с краев строки. Пример: text_4b.strip('_') = abc1234")            
        text = input("Введите текст: ")
    #metod = input("Выберите метод: ")
    #if metod == "isdigit":
        print("Текст состоит только из цифр: ", text.isdigit())
    #elif metod == "isalpha":
        print("Текст состоит только из букв: ", text.isalpha())
    #elif metod == "strip":
        n = input("Введите, какой знак убрать: ")
        print(f"{text}")
        print(f"{text.strip(n)}")
    if lvl == 5:     
        print("Уберем лишние символы, исправим пробелы и сделаем каждое слово с большой буквы в тексте '----PY+Hon;is;AWESome-----'.")
        print("Будем использовать ранее изученные методы.")
        text = "----PY+Hon;is;AWESome-----"
        print(f"{text}")
        text1 = text.strip(" -,.")
        text2 = text1.replace(";"," ")
        n = " "
        text3 = n.join(text2.split())
        print(f"{text3.title()}")
        
    
