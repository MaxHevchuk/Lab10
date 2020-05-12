# 1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем натурального числа n.
# Гевчук Максим КН-А

import timeit
from memory_profiler import profile


@profile
def recursion(n):
    """if n == 0:
        return 1
    else:
        return n * recursion(n - 1)"""

    # число буде відніматись на 1 та перемножуватись доки не буде == 0
    return 1 if n == 0 else n * recursion(n - 1)


# @profile
def iteration(n):
    # те ж саме з використанням ітерації
    for i in range(n - 1, 0, -1):
        n *= i
    return n


# число n буде запитуватись доки не буде введене натуральне
while True:
    try:
        num = int(input('Введіть число n:\n>>> '))
        if num > 0:
            break
        print('Введіть натуральне число!')

    except ValueError:
        print('Введіть натуральне число!')

# виведення
print(f'Результат рекурсії: {recursion(num)}')
print(f'Результат ітерації: {iteration(num)}')
print(f'Час затрачений на рекурсію: '
      f"{timeit.timeit('recursion(num)', setup='from __main__ import recursion, num', number=1)}")
print(f"Час затрачений на ітерацію: "
      f"{timeit.timeit('iteration(num)', setup='from __main__ import iteration, num', number=1)}")

# В усіх функціях обсяг використаної пам'яті варіюється від 13.3 до 13.9 МіВ
# Час розробки рекурсії переважає за час розробки ітерації
# Час виконання ітерації майже удвоє менше за час виконааня рекурсії
# Отож якщо ми працюємо з невелкими числами, то краще використовувати рекурсію за її читабельність
# Але якщо нампотрібні більші числа, то кращим варіантом буде ітерація за її швидкодію

