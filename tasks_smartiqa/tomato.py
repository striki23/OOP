class Tomato:
    states: dict[int: str] = {0: 'Отсутствует',
                              1: 'Цветение',
                              2: 'Зеленый',
                              3: 'Красный'}

    def __init__(self, _index: int) -> None:
        self._index = _index
        self._state = 0

    def grow(self) -> None:
        if not self.is_ripe():
            self._state += 1
            print(f'Томат {self._index} - {Tomato.states[self._state]}')

    def is_ripe(self) -> bool:
        if self._state == 3:
            return True


class TomatoBush:

    def __init__(self, nums: int):
        self.nums = nums
        self.tomatoes = [Tomato(num) for num in range(0, nums)]

    def grow_all(self) -> None:
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self) -> bool:
        if all(tomato.is_ripe() for tomato in self.tomatoes):
            print('Все томаты созрели')
            # Баг! Печатается дважды
            return True

    def give_away_all(self) -> None:
        if self.all_are_ripe():
            self.tomatoes = []
            print('Урожай собран')


class Gardener:

    def __init__(self, name: str, plant: TomatoBush) -> None:
        self.name = name
        self._plant = plant

    def work(self) -> None:
        self._plant.grow_all()

    def harvest(self) -> None:
        if not self._plant.all_are_ripe():
            print(f'Собирать урожай рано.'
                  f'Не все плоды {self._plant} созрели.')
        else:
            self._plant.give_away_all()

    @staticmethod
    def knowledge_base() -> None:
        with open('Gardener_knowledge_base.txt',
                  mode='r', encoding="UTF-8") as file_in:
            lines: list[str, str] = file_in.readlines()
            print(*lines)


if __name__ == "__main__":
    Gardener.knowledge_base()
    my_plant = TomatoBush(4)
    gardener_1 = Gardener('Alexander', my_plant)
    gardener_1.work()
    gardener_1.work()
    gardener_1.harvest()
    gardener_1.work()
    gardener_1.harvest()
