import string


class Alphabet:
    def __init__(self, lang: str, letters: str) -> None:
        self.lang = lang
        self.letters = letters

    def print(self) -> None:
        print(self.letters, self.letters.lower(), sep='')

    def letters_num(self) -> int:
        return len(self.letters)


class EngAlphabet(Alphabet):
    # 1. Неправильная реализация, string.ascii_uppercase это не Ваш алвафит,
    # Вы просто воспользовались этой переменной,
    # у Вас буквы хранятся в атрибуте self.letters.
    __letters_num: int = len(string.ascii_uppercase)

    def __init__(self) -> None:
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter: str) -> None:
        # 3. Здесь можно улучшить условие, лучше приведите letter
        # к верхнему регистру и проверьте только в letters
        if letter in self.letters or letter in self.letters.lower():
            print(f"Letter {letter} - It's English")
        else:
            print(f"Letter {letter} - It's NOT English")

    def letters_num(self) -> int:
        # 3. Неправильно реализован метод
        # У Вас уже есть реализации, как получить количество букв
        # в алфавите, обратитесь к метода letters_num родительского класса,
        # тогда все упростится, как только получили можете
        # присвоить EngAlphabet.__letters_num кол-во букв в алфавите.

        # return остается как есть
        return EngAlphabet.__letters_num

    @staticmethod
    def example() -> None:
        # 4. Обратите внимание, в ТЗ сказано:
        # """Создайте статический метод example(),
        # который будет возвращать пример текста на английском языке."""

        print('English text: "London is the capital of Great Britain"')


if __name__ == "__main__":
    my_alph = EngAlphabet()
    my_alph.print()
    print(my_alph.letters_num())
    my_alph.is_en_letter('F')
    my_alph.is_en_letter('Щ')
    EngAlphabet.example()
