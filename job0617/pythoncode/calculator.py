"""
__author__ = 'hogwarts19_zhl'
__time__ = '2021/3/19'
"""


class Calculator:
    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        else:
            return 0

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b != 0:
            return round(float(a)/b, 2)
        else:
            return 0

