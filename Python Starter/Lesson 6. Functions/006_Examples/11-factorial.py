# Факториалом числа n (обозначается n!) называется произведение
# всех натуральных чисел от 1 до n включительно.


# пример рекурсивной функции
def factorial(n):
    if n == 0:
        return 1  # условие выхода
    else:
        return n * factorial(n - 1)  # рекурсивный вызов


# вычисление факториала числа 5
print(factorial(5))