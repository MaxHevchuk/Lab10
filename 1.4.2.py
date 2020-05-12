# 2. Сформувати функцію, що визначатиме чи є задане натуральне число простим. Простим називається число, що більше за 1
# та не має інших дільників, окрім 1 та самого себе).
# Гевчук Максим КН-А

import timeit
# from memory_profiler import profile


# @profile
def recursion(n, k):
    # n - число; k - дільник

    # якщо число == 1 або закінчилась рекурсія (немає чисел на які ділиться задане число), то повертається True
    """if n == 1 or k == 1:
        return True
    # якщо знайдеться таке число, на яке ділиться задане, то повертається False
    if n % k == 0:
        return False
    else:
        return recursion(n, k - 1)"""

    return True if (n == 1 or k == 1) else False if n % k == 0 else recursion(n, k - 1)


# @profile
def iteration(n):
    # перебираються усі числа від 2 до n - 1 і якщо знайдеться дільник, то повернеться False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True


# число буде запитуватись доки не буде введене натуральне
while True:
    try:
        num = int(input('Введіть число n:\n>>> '))
        if num > 0:
            break
        print('Введіть натуральне число!')
    except ValueError:
        print('Введіть натуральне число!')

# True - число є простим; False - ні
print(f"Результат рекурсії: {recursion(num, num - 1)}")
print(f"Результат ітерації: {iteration(num)}")
print(f"Час роботи рекурсії: "
      f"{timeit.timeit('recursion(num, num-1)', setup='from __main__ import recursion, num', number=1)}")
print(f"Час роботи ітерації: "
      f"{timeit.timeit('iteration(num)', setup='from __main__ import iteration, num', number=1)}")

# В усіх функціях обсяг використаної пам'яті варіюється від 13.3 до 13.9 МіВ
# Час розробки рекурсії переважає за час розробки ітерації
# Час виконання ітерації майже удвоє менше за час виконааня рекурсії
# Отож у даному варіанті варто використовувати ітерацію за її кращу читабельність та швидкодію.
