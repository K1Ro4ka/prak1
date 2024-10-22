import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        if char in ['.', '!', '?']:
            time.sleep(0.5)
        else:
            time.sleep(0.03)
    print()

# Словарь для хранения описаний предметов
item_descriptions = {
    "ручка": "Простая шариковая ручка.",
    "тетрадь": "Тетрадь для лекций.",
    "ключ": "Ключ от двери.",
    "шляпа-невидимка": "Шляпа, скрывающая вас от охраны.",
    "булочки": "Свежие булочки из буфета.",
    "связка ключей": "Связка ключей, украденных у охранника."
}

# Словарь для хранения задач
tasks = {
    "level_1": "Найти ключ в ящике учительского стола.",
    "level_2": "Найти предмет, чтобы стать невидимым для охраны.",
    "level_3": "Сдать зачет преподавательнице-ведьме.",
    "level_4": "Принести булочки и объяснительные злому двойнику.",
    "level_5": "Разгадать загадку турникетов."
}

# Множество для отслеживания открытых дверей
opened_doors = set()

# Кортежи для координат объектов
coordinates = {
    "учительский стол": (1, 2),
    "буфет": (0, 1),
    "кабинет ведьмы": (2, 3)
}

def show_inventory(inventory):
    print_slow("Ваш инвентарь:")
    for item in inventory:
        print_slow(f"- {item}: {item_descriptions[item]}")

def level_1(inventory):
    print_slow("Вы просыпаетесь в пустом кабинете. Часы показывают 12 ночи.")
    show_inventory(inventory)
    print_slow("Вы видите на столе ключ. Что будете делать?")
    choice = input("1. Взять ключ.\n2. Осмотреться.\n")
    if choice == '1':
        inventory.append("ключ")
        print_slow("Вы взяли ключ и открыли дверь.")
        opened_doors.add("кабинет")
        return True
    else:
        print_slow("Вы осмотрелись, но ничего полезного не нашли.")
        return level_1(choice)

def level_2(inventory):
    print_slow("Вы выходите в коридор и видите охранника.")
    print_slow("Что будете делать?")
    choice = input("1. Попытаться пройти мимо.\n2. Вернуться в кабинет.\n")
    if choice == '2':
        print_slow("Вы вернулись в кабинет и решили поискать предмет, чтобы стать невидимым.")
        return True
    else:
        print_slow("Охранник вас заметил.")
        return False
        

def level_3(inventory):
    print_slow("Вы вспомнили про шляпу-невидимку на третьем этаже.")
    print_slow("Что будете делать?")
    choice = input("1. Незаметно снять связку ключей с охранника.\n2. Попытаться найти другой способ.\n")
    if choice == '1':
        inventory.append("связка ключей")
        print_slow("Вы сняли связку ключей и побежали на третий этаж.")
        show_inventory(inventory)
        return True
    else:
        print_slow("Вы не смогли найти другого способа.")
        return level_3(choice)

def level_4(inventory):
    print_slow("Вы нашли нужный кабинет, чем воспользуетесь чтобы открыть?")
    choice = input("1. связкой ключей.\n2. ручкой.\n3. тетрадью.\n ")
    if choice == '1':
        print_slow("Отлично. Один из ключей подошел.")
    else:
        print_slow("Хмм.. Может стоит попробовать что-то другое?")
        return level_4(inventory)
    print_slow("В кабинете вас ожидает преподавательница, превратившаяся в ведьму.")
    print_slow("Что будете делать?")
    choice = input("1. Сдать зачет.\n2. Попытаться убежать.\n")
    if choice == '1':
        print_slow("Чему равен квадратный корень из 144?")
        choice = input("1. 13.\n2. 12.\n3. 11.\n ")
        if choice == '2':
            print_slow("Верно.")
            print_slow("Сколько корней будет иметь уравнение: X^2-6x+8=0")
            choice = input("1. 1.\n2. 2.\n3. 0.\n ")
            if choice == '2':
                print_slow("Верно.")
                inventory.append("шляпа-невидимка")
                print_slow("Вы сдали зачет и получили шляпу-невидимку.")
                show_inventory(inventory)
                return True
            else:
                print_slow("Вы ошиблись и разозлили преподавателя.")
                return False
        else:
            print_slow("Вы ошиблись и разозлили преподавателя.")
            return False
    else:
        print_slow("Ведьма-преподавательница вас поймала.")
        return False
    

def level_5(inventory):
    print_slow("Вы надеваете шляпу-невидимку и спускаетесь на второй этаж.")
    print_slow("Здесь вас ожидает злой двойник педагога-организатора.")
    print_slow("Что будете делать?")
    choice = input("1. Принести булочки из буфета.\n2. Попытаться обмануть двойника.\n")
    if choice == '1':
        print_slow("Вы отправились на первый этаж в буфет.")
        print_slow("Аромат мягких булочек заставил вас чувствовать голод.")
        print_slow("Что будете делать?")
        choice = input("1. Принести булочки из буфета злому педагогу-организатору.\n2. Съесть самому.\n")
        if choice == '1':
            inventory.append("булочки")
            show_inventory(inventory)
            print_slow("Вы принесли булочки.")
            print_slow("Двойник сообщил вам, где заточен настоящий добрый педагог-организатор.")
            return True
        else:
          print_slow("Вы разозлили двойника педагога-организатора.")  
          return False
    else:
        print_slow("Двойник вас раскусил.")
        return False
    
def level_6(inventory):
    print_slow("Вы вызволяете настоящего педагога-организатора.")
    print_slow("Он решает помочь вам и отвлекает охрану.")
    print_slow("Что будете делать?")
    choice = input("1. Разгадать загадку турникетов.\n2. Попытаться пройти мимо турникетов.\n")
    if choice == '1':
        print_slow("Введите код для турникетов: (подсказка: номер группы)")
        code = input()
        if code == "П523":
            print_slow("Вы разгадали загадку и выбрались из техникума.")
            print_slow("Поздравляем! Вы победили!")
            return True
        else:
            print_slow("Неверный код.")
            return False
    else:
        print_slow("Вы не смогли обойти турникеты.")
        return False

def main():
    inventory = ["ручка", "тетрадь"]
    print_slow("Добро пожаловать в игру 'Московский приборостроительный техникум'.")
    if level_1(inventory):
        if level_2(inventory):
            if level_3(inventory):
                if level_4(inventory):
                     if level_5(inventory):   
                        if level_6(inventory):
                            print_slow("Спасибо за игру!")
                        else:
                            print_slow("Игра окончена.")
                     else:
                         print_slow("Игра окончена.")
                else:
                    print_slow("Игра окончена.")
            else:
                print_slow("Игра окончена.")
        else:
            print_slow("Игра окончена.")
    else:
        print_slow("Игра окончена.")
if __name__ == "__main__":
    main()