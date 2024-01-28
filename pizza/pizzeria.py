class BasePizza:
    """
    Базовый класс для пиццы.
    """

    def __init__(self, attributes):
        """
        Конструктор класса BasePizza.

        :param attributes: Словарь атрибутов пиццы (тесто, соус, начинка, цена).
        """
        self.attributes = attributes

    def __str__(self):
        """
        Метод для представления объекта в виде строки.

        :return: Строка с атрибутами пиццы.
        """
        return ", ".join(f"{key}: {value}" for key, value in self.attributes.items())

    @staticmethod
    def prepare():
        """
        Статический метод для подготовки пиццы.

        :return: Сообщение о начале приготовления.
        """
        return "Старт приготовления пиццы."

    @staticmethod
    def bake():
        """
        Статический метод для запекания пиццы.

        :return: Сообщение о запекании пиццы.
        """
        return "Пицца в духовке."

    @staticmethod
    def cut():
        """
        Статический метод для разделывания пиццы.

        :return: Сообщение о разделывании пиццы.
        """
        return "Разделываем пиццу."

    @staticmethod
    def package():
        """
        Статический метод для упаковки пиццы.

        :return: Сообщение о упаковке пиццы.
        """
        return "Пицца упакована."


class Margherita(BasePizza):
    """
    Класс для пиццы "Маргарита".
    """

    def __init__(self):
        super().__init__({"Тесто": "Традиционное",
                          "Соус": "Маринара",
                          "Начинка": "Моцарелла",
                          "Цена": 7.5})


class Hawaiian(BasePizza):
    """
    Класс для пиццы "Гавайская".
    """

    def __init__(self):
        super().__init__({"Тесто": "Стандартное",
                          "Соус": "Томатный",
                          "Начинка": "Ветчина и ананас",
                          "Цена": 8.0})


class Veggie(BasePizza):
    """
    Класс для пиццы "Овощи".
    """

    def __init__(self):
        super().__init__({"Тесто": "Тонкое",
                          "Соус": "Песто",
                          "Начинка": "Овощи",
                          "Цена": 9.0})


class PizzaOrder:
    """
    Класс для заказа пиццы.
    """

    def __init__(self):
        self.pizzas = []  # Список заказанных пицц

    def add_pizza(self, pizza):
        """
        Метод для добавления пиццы в заказ.

        :param pizza: Объект пиццы для добавления.
        """
        self.pizzas.append(pizza)

    def total_cost(self):
        """
        Метод для подсчета общей стоимости заказа.

        :return: Общая стоимость заказа.
        """
        return sum(pizza.attributes["Цена"] for pizza in self.pizzas)


class OrderTerminal:
    """
    Класс для обработки заказов.
    """

    def __init__(self):
        self.options = {
            1: Margherita(),
            2: Hawaiian(),
            3: Veggie()
        }  # Меню доступных пицц

    def show_menu(self):
        """
        Метод для отображения меню доступных пицц.
        """
        for number, pizza in self.options.items():
            print(f"{number}: {pizza}")

    def take_order(self):
        """
        Метод для оформления заказа.

        :return: Объект заказа.
        """
        order = PizzaOrder()
        while True:
            self.show_menu()
            choice = input("Выберите пиццу.\n'готово/отмена' для завершения: ")

            if choice == 'отмена':
                print("Жаль, ждем вас снова!\n")
                exit()

            if choice == 'готово':
                break

            if choice.isalpha():
                print("Введите корректный параметр.\n")
                continue

            choice = int(choice)
            if choice in self.options:
                order.add_pizza(self.options[choice])
                print("Пицца добавлена в заказ.\n")
            else:
                print("Выберите корректный номер.\n")
        return order

    def process_payment(self, order):
        """
        Метод для обработки оплаты заказа.

        :param order: Объект заказа.
        """
        total = order.total_cost()
        print(f"К оплате: {total} руб.")
        payment = float(input("Введите сумму оплаты: "))
        if payment >= total:
            print("Оплата прошла успешно.")
            change = payment - total
            if change > 0:
                print(f"Ваша сдача: {change} руб.\n")
            self.prepare_order(order)
        else:
            print("Недостаточно средств. Отмена заказа.\n")

    def prepare_order(self, order):
        """
        Метод для подготовки заказа.

        :param order: Объект заказа.
        """
        for pizza in order.pizzas:
            print(pizza.prepare(), pizza.bake(), pizza.cut(), pizza.package())


if __name__ == '__main__':
    # Пример использования
    terminal = OrderTerminal()
    order = terminal.take_order()
    terminal.process_payment(order)
