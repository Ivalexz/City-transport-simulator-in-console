import random
from CategoriesOfTransport import Bus, Tram, Trolleybus
from Tram_schedule import TransportInformation


class Route:
    def __init__(self, name, stops):
        self.name = name
        self.stops = stops

    def showRoute(self):
        print(f"Маршрут: {self.name}")
        for index, stop in enumerate(self.stops):
            print(f"{index + 1}. {stop}")


class Schedule:
    def __init__(self, transport, route, interval_between_stops):
        self.transport = transport
        self.route = route
        self.interval_between_stops = interval_between_stops
        self.current_time = 8 * 60  # Початковий час
        self.end_time = 22 * 60  # Кінцевий час

    def convert_minutes_to_time(self, total_minutes):
        #Конвертуємо хвилини у формат години:хвилини
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours:02d}:{minutes:02d}"

    def simulate(self):
        print(
            f"Симуляція маршруту {self.route.name} для {self.transport.model} (Швидкість: {self.transport.speed} км/год)")

        while self.current_time < self.end_time:
            for i, stop in enumerate(self.route.stops):
                if self.current_time >= self.end_time:
                    break

                delay = random.randint(-3, 3)  # Генеруємо затримку або випередження в хвилинах
                self.current_time += self.interval_between_stops + delay

                formatted_time = self.convert_minutes_to_time(self.current_time)
                status = "на часі" if delay == 0 else f"{'запізнення' if delay > 0 else 'випередження'} на {abs(delay)} хвилин"
                print(f"Прибуття на зупинку {stop}: {formatted_time} ({status})")



# Створюємо маршрути та зупинки від євгена бо поки не зрозомів як то передати
bus_route = Route("Автобусний маршрут №1",
                  ["Паркова алея", "Площа Незалежності", "Залізничний вокзал", "Автобусний вокзал"])
tram_route = Route("Трамвайний маршрут №2", ["Ринкова площа", 'Парковий комплекс "Сосновий бір"', 'Ботанічний сад',
                                             "Спортивний комплекс 'Арена'"])

# Створюємо транспорт (використовуємо класи з файлу Євгена)
bus = Bus('Nissan', 60, 600, 6)
tram = Tram('Tram', 45, 600, 6)
trolleybus = Trolleybus('Ford', 20, 600, 6)

# Встановлюємо розклад (інтервал між зупинками в хвилинах)
bus_schedule = Schedule(bus, bus_route, 10)
tram_schedule = Schedule(tram, tram_route, 12)


print("\n=== Симуляція для автобуса ===")
bus_schedule.simulate()

print("\n=== Симуляція для трамвая ===")
tram_schedule.simulate()

#  додати симуляцію для тролейбуса поки таку
trolleybus_route = Route("Тролейбусний маршрут №3",
                         ["Паркова алея", "Площа Незалежності", "Залізничний вокзал", "Автобусний вокзал"])
trolleybus_schedule = Schedule(trolleybus, trolleybus_route, 8)

print("\n=== Симуляція для тролейбуса ===")
trolleybus_schedule.simulate()

# це просто переписав з євгена але добавив трулейбос але поки непоміняємо зупинки
bus_info = TransportInformation('Автобус', "Паркова алея", "Автобусний вокзал")
bus_info.showInfo()

tram_info = TransportInformation('Трамвай', "Ринкова площа", "Спортивний комплекс 'Арена'")
tram_info.showInfo()

trolleybus_info = TransportInformation('Тролейбус', "Паркова алея", "Автобусний вокзал")
trolleybus_info.showInfo()