class RomanNumber:
    """
    Класс для работы с римскими и арабскими числами.
    """

    def __init__(self, value):
        """
        Инициализация объекта RomanNumber.

        :param value: Значение в виде целого числа или римской строки.
        :type value: int or str

        :raises TypeError: Если значение не является целым числом или строкой римского числа.
        """
        if isinstance(value, int):
            self.value = value
            self.roman = self._to_roman(value)
        elif isinstance(value, str):
            self.roman = value.upper()
            self.value = self._to_arabic(value.upper())
        else:
            raise TypeError("Value must be an integer or string")

    def _to_roman(self, num):
        """
        Преобразование арабского числа в римское.

        :param num: Арабское число.
        :type num: int

        :return: Римская строка числа.
        :rtype: str
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num

    def _to_arabic(self, rom):
        """
        Преобразование римской строки в арабское число.

        :param rom: Римская строка числа.
        :type rom: str

        :return: Арабское значение числа.
        :rtype: int
        """
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(rom)):
            if i > 0 and rom_val[rom[i]] > rom_val[rom[i - 1]]:
                int_val += rom_val[rom[i]] - 2 * rom_val[rom[i - 1]]
            else:
                int_val += rom_val[rom[i]]
        return int_val

    def __str__(self):
        """
        Возвращает римскую строку числа в виде строки.

        :return: Римская строка числа.
        :rtype: str
        """
        return self.roman

    def __repr__(self):
        """
        Возвращает строковое представление объекта RomanNumber.

        :return: Строковое представление объекта.
        :rtype: str
        """
        return f"RomanNumber('{self.roman}')"

    def __add__(self, other):
        """
        Перегрузка оператора сложения (+) для объектов RomanNumber.

        :param other: Другой объект RomanNumber.
        :type other: RomanNumber

        :return: Новый объект RomanNumber с результатом сложения.
        :rtype: RomanNumber

        :raises TypeError: Если операнд не является объектом RomanNumber.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.value + other.value)
        else:
            raise TypeError("Операнды должны быть римскими числами")

    def __sub__(self, other):
        """
        Перегрузка оператора вычитания (-) для объектов RomanNumber.

        :param other: Другой объект RomanNumber.
        :type other: RomanNumber

        :return: Новый объект RomanNumber с результатом вычитания.
        :rtype: RomanNumber

        :raises TypeError: Если операнд не является объектом RomanNumber.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.value - other.value)
        else:
            raise TypeError("Операнды должны быть римскими числами")

    def __mul__(self, other):
        """
        Перегрузка оператора умножения (*) для объектов RomanNumber.

        :param other: Другой объект RomanNumber.
        :type other: RomanNumber

        :return: Новый объект RomanNumber с результатом умножения.
        :rtype: RomanNumber

        :raises TypeError: Если операнд не является объектом RomanNumber.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.value * other.value)
        else:
            raise TypeError("Операнды должны быть римскими числами")

    def __truediv__(self, other):
        """
        Перегрузка оператора деления (/) для объектов RomanNumber.

        :param other: Другой объект RomanNumber.
        :type other: RomanNumber

        :return: Новый объект RomanNumber с целочисленным результатом деления.
        :rtype: RomanNumber

        :raises TypeError: Если операнд не является объектом RomanNumber.
        """
        if isinstance(other, RomanNumber):
            return RomanNumber(self.value // other.value)
        else:
            raise TypeError("Операнды должны быть римскими числами")


if __name__ == '__main__':
    # Создаем объекты RomanNumber
    roman1 = RomanNumber("IV")
    roman2 = RomanNumber("XII")
    roman3 = RomanNumber(7)

    # Выводим объекты
    print(roman1)  # "IV"
    print(roman2)  # "XII"
    print(roman3)  # "VII"

    # Выполняем математические операции
    result1 = roman1 + roman2  # "XVI"
    result2 = roman2 - roman1  # "VIII"
    result3 = roman2 * roman3  # "LXXXIV"
    result4 = roman3 / roman1  # "I"

    print('Результаты: ')
    # Выводим результаты
    print(result1)  # "XVI"
    print(result2)  # "VIII"
    print(result3)  # "LXXXIV"
    print(result4)  # "I"
