import random
from typing import Iterable
from data.hangman_pics import HangmanPics
from game_status import GameStatus
from invalid_operation_error import InvalidOperationError


class Game:

    def __init__(self):
        self.__allowed_misses = 6
        self.__tries_counter = 0
        self.__tried_letters = []
        self.__open_indexes = []
        self.__game_status = GameStatus.NOT_STARTED
        self.__word = ""

    def generate_word(self) -> str:
        """
        Генерация случайного слова для раунда
        :return: self.__word: str
        """
        filename = "data/WordsRus.txt"

        words = []
        with open(filename, encoding='utf8') as file:
            for line in file:
                words.append(line.strip("\n"))

        rand_index = random.randint(0, len(words) - 1)
        self.__word = words[rand_index]

        self.__open_indexes = [False for _ in self.__word]

        # открываем 1-2 случайные буквы в начале игры
        if len(self.__open_indexes) > 5:
            self.__open_indexes[random.randint(0, len(self.__open_indexes) - 1)] = True
            self.__open_indexes[random.randint(0, len(self.__open_indexes) - 1)] = True
        else:
            self.__open_indexes[random.randint(0, len(self.__open_indexes) - 1)] = True

        self.__game_status = GameStatus.IN_PROGRESS

        return self.__word

    def start_board(self) -> Iterable[str]:
        """
        Генерация начального поля
        :return: board: Iterable[str]
        """
        start = []
        for i, val in enumerate(self.word):
            cur_letter = val
            if self.__open_indexes[i]:
                start.append(cur_letter)
            else:
                start.append("_")
        return HangmanPics(''.join(start)).hangman_pics[0]

    def guess_letter(self, letter: str) -> Iterable[str]:
        """
        Проверяем введенную букву, если такая имеется, то открываем ее
        :param letter: str
        :return: hangman_pics: Iterable[str]
        """
        if self.tries_counter == self.allowed_misses:
            raise InvalidOperationError(f'Превышено максимальное число промахов. Допустимо {self.allowed_misses}')

        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationError(f"несоответствующий статус игры: {self.game_status}")

        open_any = False
        result = []

        for i, val in enumerate(self.word):
            cur_letter = val
            if cur_letter == letter:
                self.__open_indexes[i] = True
                open_any = True

            if self.__open_indexes[i]:
                result.append(cur_letter)
            else:
                result.append("_")

        if not open_any:
            self.__tries_counter += 1

        self.__tried_letters.append(letter)

        # изменение статуса игры, если игрок выйграл или проиграл
        if self.__is_winning():
            self.__game_status = GameStatus.WON
        elif self.tries_counter == self.allowed_misses:
            self.__game_status = GameStatus.LOST

        return HangmanPics(''.join(result)).hangman_pics[self.__tries_counter]

    def __is_winning(self):
        """
        Проверка, выйграл ли игрок
        :return: bool
        """
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
