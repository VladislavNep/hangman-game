import random
from typing import Iterable

from GameStatus import GameStatus
from InvalidOperationError import InvalidOperationError


class Game:

    def __init__(self, allowed_misses: int = 6):

        if 8 < allowed_misses < 5:
            raise ValueError("число попыток доложно быть не менее 5 и не более 8.")

        self.__allowed_misses = allowed_misses
        self.__tries_counter = 0
        self.__tried_letters = []
        self.__open_indexes = []
        self.__game_status = GameStatus.NOT_STARTED
        self.__word = ""

    def generate_word(self) -> str:
        """
        Генерация случайного слова для раунда
        :ivar None
        :return: str
        """
        filename = "data/WordsRus.txt"

        words = []
        with open(filename, encoding='utf8') as file:
            for line in file:
                words.append(line.strip("\n"))

        rand_index = random.randint(0, len(words) - 1)

        self.__word = words[rand_index]

        self.__open_indexes = [False for _ in self.__word]
        self.__game_status = GameStatus.IN_PROGRESS

        return self.__word

    def guess_letter(self, letter: str) -> Iterable[str]:
        if self.tries_counter == self.allowed_misses:
            raise InvalidOperationError(f"Превышено максимальное число промахов. Допустимо {self.allowed_misses}")

        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationError(f"несоответствующий статус игры: {self.game_status}")

        open_any = False
        result = []

        for i, c in enumerate(self.word):
            cur_letter = c
            if cur_letter == letter:
                self.__open_indexes[i] = True
                open_any = True

            if self.__open_indexes[i]:
                result.append(cur_letter)
            else:
                result.append("-")

        if not open_any:
            self.__tries_counter += 1

        self.__tried_letters.append(letter)

        if self.__is_winning():
            self.__game_status = GameStatus.WON
        elif self.tries_counter == self.allowed_misses:
            self.__game_status = GameStatus.LOST

        return result

    def __is_winning(self):
        for cur in self.__open_indexes:
            if not cur:
                return False
        return True

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def word(self) -> str:
        return self.__word

    @property
    def allowed_misses(self) -> int:
        return self.__allowed_misses

    @property
    def tries_counter(self) -> int:
        return self.__tries_counter

    @property
    def tried_letters(self) -> Iterable[str]:
        return sorted(self.__tried_letters)

    @property
    def remaining_tries(self) -> int:
        return self.allowed_misses - self.tries_counter

    @property
    def in_progress(self) -> GameStatus:
        return GameStatus.IN_PROGRESS

    @property
    def lost(self) -> GameStatus:
        return GameStatus.LOST
