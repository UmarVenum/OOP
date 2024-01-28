from abc import ABC, abstractmethod


# Абстрактный класс для стратегии расчета прибыли
class ProfitStrategy(ABC):
    @abstractmethod
    def calculate_profit(self, amount, rate, period):
        pass


# Конкретная стратегия: фиксированная прибыль
class FixedProfitStrategy(ProfitStrategy):
    def calculate_profit(self, amount, rate, period):
        return amount * rate * period / 100


# Конкретная стратегия: прибыль с бонусом
class BonusProfitStrategy(ProfitStrategy):
    def __init__(self, bonus_threshold, bonus_rate):
        self.bonus_threshold = bonus_threshold
        self.bonus_rate = bonus_rate

    def calculate_profit(self, amount, rate, period):
        profit = amount * rate * period / 100
        if amount > self.bonus_threshold:
            profit += profit * self.bonus_rate / 100
        return profit


# Конкретная стратегия: прибыль с капитализацией
class CapitalizationProfitStrategy(ProfitStrategy):
    def calculate_profit(self, amount, rate, period):
        return amount * ((1 + rate / 100) ** period - 1)


# Класс для хранения информации о депозите
class Deposit:
    def __init__(self, amount, rate, period, strategy: ProfitStrategy):
        self.amount = amount
        self.rate = rate
        self.period = period
        self.strategy = strategy

    def calculate_profit(self):
        return self.strategy.calculate_profit(self.amount, self.rate, self.period)


# Класс советчика по депозитам
class DepositAdvisor:
    def advise(self, amount, period):
        if amount < 5000:
            return Deposit(amount, 5, period, FixedProfitStrategy())
        elif 5000 <= amount < 10000:
            return Deposit(amount, 4, period, BonusProfitStrategy(5000, 10))
        else:
            return Deposit(amount, 3, period, CapitalizationProfitStrategy())


if __name__ == '__main__':
    # Пример использования
    advisor = DepositAdvisor()
    deposit = advisor.advise(7000, 3)
    print("Прибыль депозита:", deposit.calculate_profit())
