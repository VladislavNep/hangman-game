class HangmanPics:

    def __init__(self, result):
        """
        Графическое представление виселицы
        :param result:
        """
        self.result = result
        self.hangman_pics = [f'''
      {self.result}
          +---+
          |   |
              |
              |
              |
              |
      =========''', f'''
      {self.result}
         +---+
         |   |
         O   |
             |
             |
             |
      =========''', f'''
      {self.result}
         +---+
         |   |
         O   |
         |   |
             |
             |
      =========''', f'''
      {self.result}
         +---+
         |   |
         O   |
        /|   |
             |
             |
      =========''', f'''
      {self.result}
         +---+
         |   |
         O   |
        /|\  |
             |
             |
      =========''', f'''
      {self.result}
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
      =========''', f'''
      {self.result}
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
      =========''']
