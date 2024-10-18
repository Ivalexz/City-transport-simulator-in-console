from Tram_schedule import TransportInformation

obj = TransportInformation('simple transport')

def if_one():
    obj.show_all_routes()

def if_two():
    print('Ви перейшли на сторінку роботи з маршрутами і зупинками. Що Вас цікавить?')
    choice_what_to_do = 0
    while choice_what_to_do == 0:
        try:
            print()
            choice_what_to_do = int(input('1 - додати маршрут \n2 - видалити маршрут \n3 - переглянути певний маршрут \n4 - додати зупинку \n5 - видалити зупинку \n6 - вийти з сторінки \nВаш вибір:'))
        except ValueError:
            print('Ввід команд здійснюється числами')
            continue
        if choice_what_to_do==1:
            number_of_stops=0
            while number_of_stops==0:
                try:
                    number_of_stops=int(input('Кількість зупинок у вашому маршруті: '))
                except ValueError:
                    print('Будь ласка, введіть число')
                    continue
            for_transport=input('Транспорт для якого додається маршрут: ')
            obj.add_route(number_of_stops, for_transport)
            choice_what_to_do=0

        if choice_what_to_do==2:
            route_num_to_delete=0
            while route_num_to_delete==0:
                try:
                    route_num_to_delete=int(input('Номер маршруту, який бажаєте видалити: '))
                except ValueError:
                    print('Будь ласка, введіть число')
                    continue
            try:
                obj.delete_route(route_num_to_delete)
            except IndexError:
                print()
            choice_what_to_do = 0

        if choice_what_to_do==3:
            route_num=0
            while route_num == 0:
                try:
                    route_num = int(input('Введіть номер маршруту: '))
                except ValueError:
                    print('Будь ласка, введіть число')
                    continue
            obj.show_route(route_num)

        if choice_what_to_do==4:
            user_choice_route=0
            while user_choice_route == 0:
                try:
                    user_choice_route = int(input('Введіть номер маршруту у який хочете додати зупинку: '))
                except ValueError:
                    print('Будь ласка, введіть число')
                    continue
            new_stop_name=input('Введіть назву нової зупинки: ')
            where_add_stop=0
            while where_add_stop == 0:
                try:
                    where_add_stop=int(input('На яке місце хочете добавити зупинку? Зверніть увагу, якщо ви введете неіснуюче місце, зупинку буде добавлено у кінець: '))
                except ValueError:
                    print('Будь ласка, введіть число')
                    continue

            obj.add_stop(user_choice_route, new_stop_name, where_add_stop)

        if choice_what_to_do == 5:
            user_choice_stop = 0
            while user_choice_stop == 0:
                try:
                    user_choice_stop = int(input('Введіть номер маршруту з якого хочете видалити зупинку: '))
                except ValueError:
                    print('Будь ласка, введіть число')
                    continue
            where_remove_stop = 0
            while where_remove_stop == 0:
                try:
                    where_remove_stop = int(input('Місце, з якого хочете видалити зупинку: '))
                except ValueError:
                    print('Будь ласка, введіть число')
                    continue
            obj.remove_stop(user_choice_stop, where_remove_stop)

        if choice_what_to_do == 6:
            print("Повернення до головного меню...")
            break

def output_routes_func():
    print('Вітаємо у симуляторі міського транспорту у консолі! Меню:')
    start_users_choice=0
    while start_users_choice==0:
        try:
            print()
            start_users_choice=int(input('1 - переглянути список маршрутів \n2 - робота з маршрутами і зупинками \n3 - переглянути симуляцію руху \n4 - завершити \nВаш вибір:'))
        except ValueError:
            print('Ввід команд здійснюється числами')
            continue
        if start_users_choice==1:
            if_one()
            start_users_choice = 0
        elif start_users_choice==2:
            if_two()
            start_users_choice = 0
        elif start_users_choice==3:
            print(3)
        elif start_users_choice == 4:
            print('Завершення...')
            break
        else:
            print('Такої команди не існує')
            start_users_choice=0

output_routes_func()
