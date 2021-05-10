import numpy as np

def guess(*args):
    count = 0
    low = 0
    high = 101
    predict = (low + high) // 2

    while predict != number:
        count += 1
        print('Мы угадываем', predict)
        if predict < number:
            low = predict
        else:
            high = predict
        predict = (low + high) // 2
    return(count)

number = np.random.randint(1, 101)
print("Загадано число от 1 до 100")
print('Загаданное число', number)
print(f'Число было угадано за {guess(number)} попыток')

def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(guess())
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(guess)

