from Game import Game


def chars_list_to_str(chars):
    return ''.join(chars)


game = Game()
word = game.generate_word()

letters_count = len(word)

print(f"Слово состоит из {letters_count} букв")
print("Попробуй угадать слово буква за буквой")

while game.game_status == game.in_progress:
    letter = input("Выбери букву")
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))

    print(f"Оставшиеся попытки: {game.remaining_tries}")
    print(f"Использованные буквы: {chars_list_to_str(game.tried_letters)}")

if game.game_status == game.lost:
    print("Вы проиграли")
    print(f"Загаданное слово: {game.word}")
else:
    print("Невероятно, вы отгадали слово!")
