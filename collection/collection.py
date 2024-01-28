import json
from simple_class.date import Date


class DateCollection:
    def __init__(self):
        self.dates = []

    def add(self, date):
        if isinstance(date, Date):
            self.dates.append(date)
        else:
            raise TypeError("Only Date objects can be added")

    def remove(self, index):
        if 0 <= index < len(self.dates):
            return self.dates.pop(index)
        raise IndexError("Index out of range")

    def __getitem__(self, key):
        return self.dates[key]

    def __str__(self):
        return '\n'.join(f"Date {idx}: {date}" for idx, date in enumerate(self.dates))

    def save(self, filename):
        with open(filename, 'w') as file:
            dates_as_str = [str(date) for date in self.dates]
            json.dump(dates_as_str, file)

    def load(self, filename):
        with open(filename, 'r') as file:
            dates_as_str = json.load(file)
            self.dates = [Date.from_string(date_str) for date_str in dates_as_str]


def main():
    collection = DateCollection()
    collection.add(Date(2021, 12, 31))
    collection.add(Date(2022, 1, 1))
    collection.add(Date(2023, 2, 2))
    print(collection)

    print(collection[0])  # Получение первой даты из коллекции

    collection.remove(0)  # Удаление первой даты

    print('Сохранение в файл: ')
    print(collection)
    collection.save("dates.json")

    new_collection = DateCollection()
    new_collection.load("dates.json")
    print('После загрузки: ')
    print(new_collection)


if __name__ == "__main__":
    main()
