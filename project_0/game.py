"""Игра - Угадай число ПК-user (промежуточный файл)"""

import numpy as np

number = np.random.randint(1, 101) # Загадываем число
count = 0 # Создаём переменную-счётчик для учёта количества попыток

#Цикл, который будет позволять вводить и угадывать числа. 
#Цикл будет работать до тех пор, пока пользователь не угадает загаданное число. 
#Вводить число пользователь будет с клавиатуры, через input (в консоли будет выведено приглашение ввести число).

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100: 10")) # Число, по предположению пользователя, загаданное программой

# Проверим, соответствует ли введённое пользователем число (predict_number) загаданному

    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла