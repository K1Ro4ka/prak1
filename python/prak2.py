users = [  # Список словарей для сотрудников и посетителей
    {
        'username': 'kira',  
        'password': '1234',  
        'role': 'пользователь',          
        'history': [],           
        'created_at': '2024-09-01'  
    },
    {
        'username': 'admin',  
        'password': '4321',  
        'role': 'администратор' 
    }
]

attractions = [  # Список словарей для аттракционов
    {
        'name': 'Американские горки',  
        'price': 500,  
        'rating': 4.5,  
        'created_at': '2024-09-01'  
    },
    {
        'name': 'Колесо обозрения', 
        'price': 300,  
        'rating': 4.0,  
        'created_at': '2024-09-02'  
    }
]

current_user = None

def login():
    print("Здраствуйте! Чтобы войти в систему необходимо вести свой логин и пароль")
    global current_user
    username = input("Логин: ")
    password = input("Пароль: ")

    for user in users:  
        if user['username'] == username and user['password'] == password:  # Словарь
            current_user = user  # Словарь
            print(f"Добро пожаловать, {username}!")
            return
    print("Неверный логин или пароль.")

def view_attractions():
    for attraction in attractions:  # Список словарей
        print(f"{attraction['name']} - Цена: {attraction['price']} руб., Рейтинг: {attraction['rating']}")  # Словарь

def buy_attraction():
    view_attractions()
    name = input("Введите название аттракциона для покупки: ")
    for attraction in attractions: 
        if attraction['name'] == name:  # Словарь
            current_user['history'].append(attraction['name'])  # Словарь
            print(f"Вы купили аттракцион '{name}'.")
            return
    print("Аттракцион не найден.")

def view_history():
    print("История посещений:")
    for attraction in current_user['history']:  # Словарь
        print(attraction)

def sort_attractions_by_price():
    sorted_attractions = sorted(attractions, key=lambda x: x['price'])  
    for attraction in sorted_attractions:  # Список словарей
        print(f"{attraction['name']} - Цена: {attraction['price']} руб.")  # Словарь

def sort_attractions_by_rating():
    sorted_attractions = sorted(attractions, key=lambda x: x['rating'], reverse=True)  
    for attraction in sorted_attractions:  # Список словарей
        print(f"{attraction['name']} - Рейтинг: {attraction['rating']}")  # Словарь

def update_profile():
    new_password = input("Введите новый пароль: ")
    current_user['password'] = new_password  # Словарь
    print("Пароль успешно изменен.")

def add_attraction():
    name = input("Название аттракциона: ")
    price = float(input("Цена: "))
    rating = float(input("Рейтинг: "))
    attractions.append({ 
        'name': name,  # Словарь
        'price': price,  # Словарь
        'rating': rating,  # Словарь
        'created_at': '2024-09-01'  # Словарь
    })
    print(f"Аттракцион '{name}' добавлен.")

def delete_attraction():
    view_attractions()
    name = input("Введите название аттракциона для удаления: ")
    for attraction in attractions:  
        if attraction['name'] == name:  # Словарь
            attractions.remove(attraction)  
            print(f"Аттракцион '{name}' удален.")
            return
    print("Аттракцион не найден.")

def edit_attraction():
    view_attractions()
    name = input("Введите название аттракциона для редактирования: ")
    for attraction in attractions:  
        if attraction['name'] == name:  # Словарь
            while True:
                print("Что вы хотите изменить?")
                print("1-цена")
                print("2-рейтинг")
                try:
                    choice = int(input())
                    if choice < 1 or choice > 2:
                        print("Неверный выбор действия. Введите число от 1 до 2.")
                        continue
                except ValueError:
                    print("Пожалуйста, введите число от 1 до 2.")
                    continue

                if choice == 1:
                    new_price = float(input("Новая цена: "))
                    attraction['price'] = new_price  # Словарь
                    print(f"Цена аттракциона '{name}' обновлена.")
                    break
                elif choice == 2:
                    new_rating = float(input("Новый рейтинг: "))
                    attraction['rating'] = new_rating  # Словарь
                    print(f"Рейтинг аттракциона '{name}' обновлен.")
                    break
            return
    print("Аттракцион не найден.")

def manage_users():
    print("Управление пользователями:")
    for user in users:  
        print(f"{user['username']} - Роль: {user['role']}")  # Словарь
    action = input("Выберите действие: 1-добавить пользователя, 2-удалить пользователя, 3-редактировать пользователя.")
    if action == '1':
        username = input("Логин: ")
        password = input("Пароль: ")
        role = input("Роль (пользователь/администратор): ")
        users.append({  # Список словарей
            'username': username,  # Словарь
            'password': password,  # Словарь
            'role': role,  # Словарь
            'history': [],  # Словарь
            'created_at': '2024-09-01'  # Словарь
        })
        print(f"Пользователь '{username}' добавлен.")
    elif action == '2':
        username = input("Логин пользователя для удаления: ")
        for user in users:  
            if user['username'] == username:  # Словарь
                users.remove(user)  
                print(f"Пользователь '{username}' удален.")
                return
        print("Пользователь не найден.")
    elif action == '3':
        username = input("Логин пользователя для редактирования: ")
        for user in users:  
            if user['username'] == username:  # Словарь
                new_password = input("Новый пароль: ")
                user['password'] = new_password  # Словарь
                print(f"Пароль пользователя '{username}' обновлен.")
                return
        print("Пользователь не найден.")

def view_statistics():
    print("Статистика:")
    print(f"Количество аттракционов: {len(attractions)}")  
    print(f"Количество пользователей: {len(users)}")  
    total_visits = sum(len(user.get('history', [])) for user in users)  
    print(f"Общее количество посещений: {total_visits}")

def user_menu():
    while True:
        print("Выберите действие:")
        print("1-просмотреть доступные аттракционы")
        print("2-купить аттракцион")
        print("3-просмотреть историю посещений")
        print("4-сортировать аттракционы по цене")
        print("5-сортировать аттракционы по рейтингу")
        print("6-обновить профиль")
        print("7-выйти")
        try:
            choice = int(input())
            if choice < 1 or choice > 7:
                print("Неверный выбор действия. Введите число от 1 до 7.")
                continue
        except ValueError:
            print("Пожалуйста, введите число от 1 до 7.")
            continue

        if choice == 1:
            view_attractions()
        elif choice == 2:
            buy_attraction()
        elif choice == 3:
            view_history()
        elif choice == 4:
            sort_attractions_by_price()
        elif choice == 5:
            sort_attractions_by_rating()
        elif choice == 6:
            update_profile()
        elif choice == 7:
            break

def admin_menu():
    while True:
        print("\nВыберите действие:")
        print("1-добавить аттракцион")
        print("2-удалить аттракцион")
        print("3-редактировать данные об аттракционе")
        print("4-управление пользователями")
        print("5-просмотреть статистику")
        print("6-выйти")
        try:
            choice = int(input())
            if choice < 1 or choice > 6:
                print("Неверный выбор действия. Введите число от 1 до 6.")
                continue
        except ValueError:
            print("Пожалуйста, введите число от 1 до 6.")
            continue

        if choice == 1:
            add_attraction()
        elif choice == 2:
            delete_attraction()
        elif choice == 3:
            edit_attraction()
        elif choice == 4:
            manage_users()
        elif choice == 5:
            view_statistics()
        elif choice == 6:
            break

def main():
    global current_user
    while True:
        login()
        if current_user:
            if current_user['role'] == 'пользователь':  # Словарь
                user_menu()
            elif current_user['role'] == 'администратор':  # Словарь
                admin_menu()
            current_user = None
        else:
            print("Попробуйте войти снова.")

if __name__ == "__main__":
    main()