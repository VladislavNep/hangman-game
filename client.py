from game import Game


def chars_list_to_str(chars):
    return ''.join(chars)


game = Game()
word = game.generate_word()

letters_count = len(word)

print(f"Слово состоит из {letters_count} букв")
print("Попробуй угадать слово по буквам")
print(game.start_board())


while game.game_status == game.in_progress:
    letter = input("Выбери букву \n")

    print(game.guess_letter(letter))

    print(f"Оставшиеся попытки: {game.remaining_tries}")
    print(f"Использованные буквы: {chars_list_to_str(game.tried_letters)} \n")

if game.game_status == game.lost:
    print("Вы проиграли")
    print(f"Загаданное слово: {game.word}")
else:
    print("Невероятно, вы отгадали слово!")
