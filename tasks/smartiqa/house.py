class House:

    def __init__(self, area: float, price: float) -> None:
        self._area = area
        self._price = price

    def final_price(self, sale: int) -> float:
        # Конфликт имен, у Вас метод и переменная называются одинаково.
        # final_price: float = self._price * (1 - sale / 100)
        # return final_price
        return self._price * (1 - sale / 100)


class SmallHouse(House):
    # default_area: int = 40  # Это константное значение
    DEFAULT_AREA: int = 40  # Это константное значение

    def __init__(self, price: float) -> None:
        super().__init__(SmallHouse.DEFAULT_AREA, price)


# Я могу предположить, что Вы этот класс реализовали после,
# потому что, Вы не смогли указать аннотацию типов для классов,
# которые ещё не описаны. Если это так, Вам нужно в аннотации,
# эти классы нужно включить в кавычки, это будет работать, я исправлю,
# Вам нужно этот класс перенести наверх, до House.
class Human:
    default_name: str = 'Ivan'
    default_age: int = 21

    def __init__(self,
                 name: str = default_name,
                 age: int = default_age) -> None:
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self) -> None:
        print(f'Name: {self.name}'
              f'\nAge: {self.age}'
              f'\nMoney: {self.__money}'
              f'\nHouse: {self.__house}')

    @staticmethod
    def default_info() -> None:
        print(f'Default name: {Human.default_name}'
              f'\nDefault age:{Human.default_age}')

    def __make_deal(self, house: 'House', price: float) -> None:
        self.__money -= price
        self.__house = house

    def earn_money(self, income: int | float) -> None:
        self.__money += income

    def buy_house(self, house: 'House', sale: int) -> None:
        price: float = house.final_price(sale)
        if self.__money < price:
            print('Недостаточно денег для покупки')
            return

        self.__make_deal(house, price)


if __name__ == "__main__":
    Human.default_info()

    person1 = Human('Dasha', 33)
    person1.info()

    my_home = SmallHouse(20000)
    person1.buy_house(my_home, 10)

    person1.earn_money(50000)
    person1.buy_house(my_home, 10)
    person1.info()
