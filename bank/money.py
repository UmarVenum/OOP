from abc import ABC, abstractmethod


class MoneyTransfer(ABC):
    """
    Абстрактный базовый класс для всех видов денежных переводов.
    """

    def __init__(self, amount):
        """
        Инициализирует объект MoneyTransfer с указанной суммой.

        Args:
            amount (int): Сумма для перевода.
        """
        self.amount = amount

    @abstractmethod
    def make_transfer(self):
        """
        Абстрактный метод, который должен быть реализован в подклассах.
        """
        pass

    def __str__(self):
        """
        Строковое представление объекта MoneyTransfer.
        """
        return f"Перевод: {self.make_transfer()}"


class BankTransfer(MoneyTransfer):
    """
    Представляет банковский перевод.
    """

    def make_transfer(self):
        """
        Создает описание банковского перевода.

        Returns:
            str: Описание банковского перевода.
        """
        return f"Перевод {self.amount} через банк"


class CurrencyTransfer(MoneyTransfer):
    """
    Представляет перевод с обменом валюты.
    """

    def __init__(self, amount, currency):
        """
        Инициализирует объект CurrencyTransfer с указанной суммой и валютой.

        Args:
            amount (int): Сумма для перевода.
            currency (str): Валюта, в которой будет выполнен перевод.
        """
        super().__init__(amount)
        self.currency = currency

    def make_transfer(self):
        """
        Создает описание перевода с обменом валюты.

        Returns:
            str: Описание перевода с обменом валюты.
        """
        return f"Перевод {self.amount} в {self.currency} через валютную биржу"


class PostalTransfer(MoneyTransfer):
    """
    Представляет перевод через почту.
    """

    def make_transfer(self):
        """
        Создает описание перевода через почту.

        Returns:
            str: Описание перевода через почту.
        """
        return f"Перевод {self.amount} через почту"


class PaymentPlatformTransfer(MoneyTransfer):
    """
    Представляет перевод через платежную платформу.
    """

    def __init__(self, amount, platform):
        """
        Инициализирует объект PaymentPlatformTransfer с указанной суммой и платформой.

        Args:
            amount (int): Сумма для перевода.
            platform (str): Используемая платформа для перевода.
        """
        super().__init__(amount)
        self.platform = platform

    def make_transfer(self):
        """
        Создает описание перевода через платежную платформу.

        Returns:
            str: Описание перевода через платежную платформу.
        """
        return f"Перевод {self.amount} с использованием платформы {self.platform}"


def main():
    transfers = [
        BankTransfer(1000),
        CurrencyTransfer(500, "EUR"),
        PostalTransfer(300),
        PaymentPlatformTransfer(750, "PayPal")
    ]

    for transfer in transfers:
        print(transfer)


if __name__ == "__main__":
    main()
