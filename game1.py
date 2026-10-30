print("Лабиринт")
print()
print("Управление: w/a/s/d, i — инвентарь, q — выбросить предмет")
print()
print("Обозначения:")
print("@ — игрок (ты)")
print("M — монстр")
print("W — меч")
print("Z — зачарование")
print("A — аптечка")
print("K — ключ")
print("S — сундук")
print("L — ловушка")
print("P — портал")
print("D — дверь")
print()
input("Нажми ENTER, чтобы начать игру...")
print()

shablon = [
    ['.', '.', 'M', '.', 'K'],
    ['.', 'S', '.', 'M', '.'],
    ['M', '.', 'A', '.', 'L'],
    ['.', 'W', '.', 'Z', '.'],
    ['.', '.', 'P', '.', 'D'],
]

labirint = [line[:] for line in shablon]
portal = (1, 1)

hp = 100
x = 0
y = 0

inventar = []
zacharovano = False
kod = [c for c in [3, 7, 2]]

igra = True
khod = 0

def karta():
    print("  0 1 2 3 4")
    for i in range(5):
        stroka = ""
        for j in range(5):
            if i == x and j == y:
                stroka += "@ "
            else:
                stroka += "* "
        print(f"{i} {stroka}")

def status():
    print(f"HP: {hp}")
    print(f"Инвентарь: {inventar}")
    if zacharovano:
        print("Оружие зачаровано")

karta()
print()
status()
print()

while igra and hp > 0:
    khod += 1
    
    hod = input("Ход (w/a/s/d/i/q): ").lower()
    print()
    
    if hod == 'i':
        inventar.sort()
        print(f"sort: {inventar}")
        inventar.reverse()
        print(f"reverse: {inventar}")
        if 'ключ' in inventar:
            print(f"ключ на позиции: {inventar.index('ключ')}")
        else:
            print("ключа нет")
        print()
        continue
    
    if hod == 'q':
        if len(inventar) > 0:
            print(f"выбросил: {inventar.pop()}")
        else:
            print("инвентарь пуст")
        print()
        continue
    
    x1 = x
    y1 = y
    
    if hod == 'w':
        x1 = x - 1
    elif hod == 's':
        x1 = x + 1
    elif hod == 'a':
        y1 = y - 1
    elif hod == 'd':
        y1 = y + 1
    else:
        print("Error")
        continue
    
    if x1 < 0 or x1 >= 5 or y1 < 0 or y1 >= 5:
        print("стена")
        print()
        continue
    
    x = x1
    y = y1
    komnata = labirint[x][y]
    
    if komnata == '.':
        print("пустая комната")
    
    elif komnata == 'M':
        print("монстр")
        if zacharovano:
            print("зачарованное оружие, урон: 10")
        elif 'меч' in inventar:
            print("меч, урон: 15")
        else:
            print("без оружия, урон: 20")
            hp -= 20
        labirint[x][y] = '.'
    
    elif komnata == 'S':
        if 'ключ' in inventar:
            print("сундук открыт")
            inventar.remove('ключ')
            print("подсказка: код двери — 3, ?, 2; cумма = 12")
            labirint[x][y] = '.'
        else:
            print("сундук заперт, нужен ключ")
    
    elif komnata == 'K':
        print("ключ")
        inventar.append('ключ')
        labirint[x][y] = '.'
    
    elif komnata == 'A':
        print("аптечка +30 HP")
        hp += 30
        if hp > 100:
            hp = 100
        labirint[x][y] = '.'
    
    elif komnata == 'W':
        print("меч")
        inventar.append('меч')
        labirint[x][y] = '.'
    
    elif komnata == 'Z':
        print ("зачарование")
        if 'меч' in inventar:
            zacharovano = True
            print("оружие зачаровано")
        else:
            print("нет меча")
        labirint[x][y] = '.'
    
    elif komnata == 'L':
        print("ловушка -15 HP")
        hp -= 15
        labirint[x][y] = '.'
    
    elif komnata == 'P':
        print("портал")
        x = portal[0]
        y = portal[1]
        print(f"перемещён в ({x}, {y})")
        labirint[x][y] = '.'
    
    elif komnata == 'D':
        print("дверь")
        print ("введи код (3 цифры через пробел):")
        vod = input("код: ")
        chisla = [int(c) for c in vod.split()]
        if chisla == kod:
            print("победа")
            igra = False
        else:
            print("неверный код -10 HP")
            hp -= 10
    
    print()
    karta()
    print()
    status()
    print()
    
    if hp <= 0:
        print("ты погиб")
        igra = False

print()
print("игра окончена")
print(f"ходов: {khod}")
print(f"HP: {hp}")
print(f"инвентарь: {inventar}")