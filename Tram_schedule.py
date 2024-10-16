class TransportInformation:  #клас для транспорту та його зупинок
    def __init__(self, transport_category, first_station, last_station):
        self.transport_category=transport_category
        self.first_station=first_station
        self.last_station=last_station
        self.list_transport = []
        self.list_of_stops_bus_and_trolleybus=["Паркова алея", 'Площа Незалежності', 'Залізничний вокзал', "Автобусний вокзал"] #ІМПРОВІЗОВАНИЙ СПИСОК [ПОТРІБНО РЕДАГУВАТИ]
        self.list_of_stops_tram = ["Ринкова площа", 'Парковий комплекс "Сосновий бір"', 'Ботанічний сад', "Спортивний комплекс 'Арена'"]  # ІМПРОВІЗОВАНИЙ СПИСОК [ПОТРІБНО РЕДАГУВАТИ]
    def showInfo(self):
        print(f"Транспорт: {self.transport_category} \nПерша зупинка: {self.first_station} \nКінцева зупинка: {self.last_station}")
        self.list_transport.append((self.transport_category))
        try:
            show_list_of_stops=int(input("Якщо хочете дізнатися про всі зупинки цього транспорту - тисніть 1: "))
            if show_list_of_stops==1:
                if self.transport_category=="Автобус" or self.transport_category=="Тролейбус":
                    print('Перелік зупинок:')
                    for index, i in enumerate(self.list_of_stops_bus_and_trolleybus): #ЗМІНИТИ НАЗВУ ЗМІННОЇ ВІДПОВІДНО ДО ФАЙЛУ ЄВГЕНА
                       print(f"{index+1} - {i}")
                elif self.transport_category=='Трамвай':
                    print('Перелік зупинок:')
                    for index, i in enumerate(self.list_of_stops_tram): #ЗМІНИТИ НАЗВУ ЗМІННОЇ ВІДПОВІДНО ДО ФАЙЛУ ЄВГЕНА
                       print(f"{index+1} - {i}")
            else:
                print()

        except ValueError: # Якщо користувач вводить не число
            print()

bus=TransportInformation('Автобус', "Паркова алея", "Автобусний вокзал")
bus.showInfo()
print()
tram=TransportInformation('Трамвай', "Ринкова площа", "Спортивний комплекс 'Арена'")
tram.showInfo()
print()
trolleybus=TransportInformation('Тролейбус', "Паркова алея", "Автобусний вокзал")
trolleybus.showInfo()
