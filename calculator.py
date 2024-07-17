import logging
from logger import setup_logger

setup_logger()

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

class ComplexCalculator:
    def add(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        logging.info(f"Сложение {a} и {b}")
        return ComplexNumber(a.real + b.real, a.imag + b.imag)

    def multiply(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        logging.info(f"Умножение {a} и {b}")
        real = a.real * b.real - a.imag * b.imag
        imag = a.real * b.imag + a.imag * b.real
        return ComplexNumber(real, imag)

    def divide(self, a: ComplexNumber, b: ComplexNumber) -> ComplexNumber:
        logging.info(f"Деление {a} на {b}")
        if b.real == 0 and b.imag == 0:
            raise ValueError("Деление на ноль невозможно")

        denominator = b.real ** 2 + b.imag ** 2
        real = (a.real * b.real + a.imag * b.imag) / denominator
        imag = (a.imag * b.real - a.real * b.imag) / denominator
        return ComplexNumber(real, imag)
