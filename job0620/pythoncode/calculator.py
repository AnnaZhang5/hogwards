"""
__author__ = 'hogwarts19_zhl'
__time__ = '2021/3/19'
"""


class Calculator:
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, float) and isinstance(b, float):
            return round((a + b), 2)
        else:
            return 0

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return round(float(a)/b, 2)


