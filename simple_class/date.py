import json
from datetime import datetime, timedelta


class Date:
    def __init__(self, year, month, day):
        """
        Инициализация объекта Date с указанным годом, месяцем и днем.

        Args:
            year (int): Год.
            month (int): Месяц (1-12).
            day (int): День (1-31).
        """
        self.year = year
        self.month = month
        self.day = day
        self.date = datetime(year, month, day)

    def __str__(self):
        """
        Возвращает строковое представление даты в формате 'ГГГГ-ММ-ДД'.
        """
        return self.date.strftime('%Y-%m-%d')

    def __add__(self, days):
        """
        Добавляет указанное количество дней к текущей дате.

        Args:
            days (int): Количество дней для добавления.

        Returns:
            Date: Новый объект Date после добавления дней.
        """
        new_date = self.date + timedelta(days=days)
        return Date(new_date.year, new_date.month, new_date.day)

    def __sub__(self, days):
        """
        Вычитает указанное количество дней из текущей даты.

        Args:
            days (int): Количество дней для вычитания.

        Returns:
            Date: Новый объект Date после вычитания дней.
        """
        new_date = self.date - timedelta(days=days)
        return Date(new_date.year, new_date.month, new_date.day)

    def __eq__(self, other):
        """
        Проверяет равенство текущей даты и другой даты.

        Args:
            other (Date): Другой объект Date.

        Returns:
            bool: True, если даты равны, иначе False.
        """
        return self.date == other.date

    def __lt__(self, other):
        """
        Проверяет, является ли текущая дата меньшей чем другая дата.

        Args:
            other (Date): Другой объект Date.

        Returns:
            bool: True, если текущая дата меньше, иначе False.
        """
        return self.date < other.date

    @classmethod
    def from_string(cls, date_string):
        """
        Создает объект Date из строки в формате 'ГГГГ-ММ-ДД'.

        Args:
            date_string (str): Строка с датой.

        Returns:
            Date: Новый объект Date из строки.
        """
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

    def save(self, filename):
        """
        Сохраняет текущую дату в файл в формате JSON.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w') as file:
            json.dump(str(self), file)

    def load(self, filename):
        """
        Загружает дату из файла JSON и устанавливает ее как текущую дату.

        Args:
            filename (str): Имя файла для загрузки.
        """
        with open(filename, 'r') as file:
            date_string = json.load(file)
            self.year, self.month, self.day = map(int, date_string.split('-'))
            self.date = datetime(self.year, self.month, self.day)


def main():
    date1 = Date(2021, 12, 31)
    print(date1)
    date2 = date1 + 1
    print(date2)
    print(date1 == date2)
    date1.save('date.json')
    new_date = Date.from_string('2020-01-01')
    new_date.load('date.json')
    print(new_date)


if __name__ == "__main__":
    main()
