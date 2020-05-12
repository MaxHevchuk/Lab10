# 3. Сформувати функцію для обчислення індексу максимального елемента масиву n*n, де 1<=n<=5.
# Гевчук Максим КН-А

import timeit
import numpy as np
# from memory_profiler import profile


# @profile
def recursion(arr, i=0, j=0, col=0, row=0):
    # i та j індекси рядків та стовпчиків відповідно, що перебираються
    # kol та row - індекси максимального елементу

    # коли рекурсія досягла останнього елементу в !рядку! то переходимо до наступного рядку з початкового елем.
    if j == len(arr[i]):
        i, j = i + 1, 0

    # якщо знайдеться елем., що більший за елем. з індексом [col, row], то змінюються значення col, row
    if arr[i][j] > arr[col][row]:
        col, row = i, j

    # коли рекурсія досягла останнього елементу в !масиві!, то повертається індекс максимального елементу
    if (i == len(arr) - 1) and (j == len(arr[i]) - 1):
        return col, row
    j += 1
    return recursion(arr, i, j, col, row)


# @profile
def iteration(arr, col=0, row=0):
    # перебираються рядки та стовпчики
    for i in range(len(arr)):
        for j in range(len(arr[i])):

            # порівнюються елементи як було в рекурсії
            if arr[i, j] > arr[col, row]:
                col, row = i, j
    return col, row


# число буде запитуватись доті, доки не буде належати заданому проміжку
while True:
    try:
        n = int(input('Введіть число n: '))

        if n in range(1, 6):
            break
        print('Введіть число в діапазоні [1, 5]')
    except ValueError:
        print('Введіть число в діапазоні [1, 5]')
        continue

# створюється масив із випадковими значеннями розміром n*n
random_arr = np.random.randint(0, 100, [n, n])

# виведення результатів
print(f'Масив:\n{random_arr}')
print(f'Результат рекурсії: {recursion(random_arr)}')
print(f'Результат ітерації: {iteration(random_arr)}')
print(f'Час затрачений на рекурсію: '
      f'{timeit.timeit("recursion(random_arr)", "from __main__ import recursion, random_arr", number=1)}')
print(f'Час затрачений на ітерацію: '
      f'{timeit.timeit("iteration(random_arr)", "from __main__ import iteration, random_arr", number=1)}')

# В усіх функціях обсяг використаної пам'яті варіюється від 13.3 до 13.9 МіВ
# Час розробки рекурсії переважає за час розробки ітерації
# Час виконання ітерації майже удвоє менше за час виконааня рекурсії
# Отож у даному варіанті варто використовувати ітерацію, тому що читабельність в неї набагато краща за рекурсію, а також
# значна різниця швидкостей.
