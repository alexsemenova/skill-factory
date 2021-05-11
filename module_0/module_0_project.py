import numpy as np


def guess(number):
    """Функция по угадыванию рандомного числа с использованием верхних и нижних
    границ диапазона и подсчетом попыток.
    С каждым шагом функция ссужает диапазон угадывания"""
    count = 0  # введем счетчик попыток
    low = 0  # нижняя граница
    high = 101  # вверхняя граница
    predict = (low + high) // 2  # берем среднее арифметическое границ за первое предполагаемое число

    while predict != number:
        count += 1  # пока не угадаем число, увеличиваем счетчик
        print('Предполагаемое число - ', predict)
        if predict < number:  # с помощью if ссужаем диапазон угадывания числа
            low = predict  # в случае, если предполагаемое число меньше загаданного, ставим его как нижнюю границу
        else:
            high = predict  # в случае, если предполагаемое число больше загаданного, ставим его как верхнюю границу
        predict = (low + high) // 2  # среднее арифметическое двух границ - новое предполагаемое число
    return count


number = np.random.randint(1, 101)
print("Загадано число от 1 до 100")
print('Загаданное число - ', number)
print(f'Число было угадано за {guess(number)} попыток')


def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(guess(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score
