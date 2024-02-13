class House:

    def __init__(self, area: float, price: float) -> None:
        self._area = area
        self._price = price

    def final_price(self, sale: int) -> float:
        final_price: float = self._price * (1 - sale/100)
        return final_price


class SmallHouse(House):

    default_area: int = 40

    def __init__(self, price: float) -> None:
        super().__init__(SmallHouse.default_area, price)


class Human:

    default_name: str = 'Ivan'
    default_age: int = 21

    def __init__(self, name=default_name, age=default_age) -> None:
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

    def __make_deal(self, house: House, price: float) -> None:
        self.__money -= price
        self.__house = house

    def earn_money(self, income) -> None:
        self.__money += income

    def buy_house(self, house: House, sale: int) -> None:
        price: float = house.final_price(sale)
        if self.__money < price:
            print('Недостаточно денег для покупки')
        else:
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
