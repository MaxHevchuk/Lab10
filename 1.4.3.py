# 3. Сформувати функцію для переведення натурального числа з десяткової системи числення у шістнадцятирічну.
# Гевчук Максим КН-А

import timeit
# from memory_profiler import profile

# словник - переведення в шістнадцятирічну систему числення
int_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
              12: 'C', 13: 'D', 14: 'E', 15: 'F'}


# @profile
def recursion(n):
    # перевіряється чи число не є більшим за 16
    """if n in range(16):
        return int_to_hex_letters[n]

    # якщо все ж таки більше, то залишок від ділення склеюється в кінець послідовності, а задане число, поділене націло,
    передається у функцію в якості нового аргументу

    else:
        return recursion(n // 16) + int_to_hex_letters[n % 16]"""

    return int_to_hex[n] if n in range(16) else recursion(n // 16) + int_to_hex[n % 16]


# @profile
def iteration(n):
    s = ''
    # той же принцип роботи, тільки з використанням ітерації
    while n != 0:
        s = str(int_to_hex[n % 16]) + s
        n //= 16
    return s


# число буде запитуватись доки не буде введене натуральне
while True:
    try:
        num = int(input('Введіть число n:\n>>> '))
        if num > 0:
            break
        print('Введіть натуральне число!')
    except ValueError:
        print('Введіть натуральне число!')

print(f"Результат рекурсії: {recursion(num)}")
print(f"Результат ітерації: {iteration(num)}")
print(f"Час роботи рекурсії: "
      f"{timeit.timeit('recursion(num)', setup='from __main__ import recursion, num', number=1)}")
print(f"Час роботи ітерації: "
      f"{timeit.timeit('iteration(num)', setup='from __main__ import iteration, num', number=1)}")

# В усіх функціях обсяг використаної пам'яті варіюється від 13.3 до 13.9 МіВ
# Час розробки рекурсії переважає за час розробки ітерації
# Час виконання ітерації майже удвоє менше за час виконааня рекурсії
# У даному випадку краще використовувати рекурсію, тому що вона краще читабельна та не дуже велика різниця часу роботи.