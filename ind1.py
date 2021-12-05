#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Объявите функцию, которая возвращает переданную ей строку
# в нижнем регистре (с малыми буквами). Определите декоратор
# для этой функции, который имеет один параметр tag, определяющий
# строку с названием тега. Этот декоратор должен заключать возвращенную
# функцией строку в тег tag и возвращать результат. Пример заключения
# строки "python" в тег h1: <h1>python</h1>. Примените
# декоратор со значением tag="div" к функции и вызовите
# декорированную функцию. Результат отобразите на экране.


def decorator(tag):
    def wrapper(func):
        def wrapped(old_str):
            low_str = func(old_str)
            result = ["<", tag, ">", low_str, "</", tag, ">"]
            return "".join(result)
        return wrapped
    return wrapper


@decorator(tag="div")
def to_low(old_str):
    low_str = [i.lower() for i in old_str]
    return "".join(low_str)


if __name__ == '__main__':
    to_low_str = input("Введите строку: ")
    print(to_low(to_low_str))
