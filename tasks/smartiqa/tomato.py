class Tomato:
    # Отлично!
    states: dict[int: str] = {0: 'Отсутствует',
                              1: 'Цветение',
                              2: 'Зеленый',
                              3: 'Красный'}

    def __init__(self, _index: int) -> None:
        self._index = _index
        self._state = 0  # Хорошая идея!

    def grow(self) -> None:
        if not self.is_ripe():
            self._state += 1
            # 1. Это лишний код, информацию выводить не нужно.
            print(f'Томат {self._index} - {Tomato.states[self._state]}')

    def is_ripe(self) -> bool:
        if self._state == 3:  # 2. В коде не используйте магические значения,
            # непонятно что будет означать 3, лучше берите длину states
            return True

        # Ещё один момент, Вам не нужно писать блок if, просто сравните
        # self._state == длина, оператор сравнения возвращает булевое значение


class TomatoBush:

    def __init__(self, num: int):
        self.num = num
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self) -> None:
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self) -> bool:
        return all(tomato.is_ripe() for tomato in self.tomatoes)
        # Лучше не печатайте лишний текст
        # print('Все томаты созрели')

        # Причина бага находится в методе give_away_all(),
        # Вы там вызываете if self.all_are_ripe():

    def give_away_all(self) -> None:
        if self.all_are_ripe():
            # self.tomatoes = []  # Плохая идея, Вы тут создаете новый список,
            # лучше очистить существующий объект списка

            self.tomatoes.clear()  # Так мы работаем всегда
            # с одним и тем же объектом списка

            # print('Урожай собран')


class Gardener:

    def __init__(self, name: str, plant: 'TomatoBush') -> None:
        self.name = name
        self._plant = plant

    def work(self) -> None:
        self._plant.grow_all()

    def harvest(self) -> None:
        if not self._plant.all_are_ripe():
            print(f'Собирать урожай рано.'
                  f'Не все плоды {self._plant} созрели.')
            return

        self._plant.give_away_all()

    @staticmethod
    def knowledge_base() -> None:
        with open('Gardener_knowledge_base.txt',
                  mode='r',
                  encoding="UTF-8") as file_in:
            # Хорошая реализация!
            # Момент, избегайте одноразовых переменных
            print(*file_in.readlines())


if __name__ == "__main__":
    Gardener.knowledge_base()
    my_plant = TomatoBush(4)
    gardener_1 = Gardener('Alexander', my_plant)
    gardener_1.work()
    gardener_1.work()
    gardener_1.harvest()
    gardener_1.work()
    gardener_1.harvest()
