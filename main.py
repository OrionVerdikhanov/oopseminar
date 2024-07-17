from calculator import ComplexNumber, ComplexCalculator

def main():
    calc = ComplexCalculator()

    a = ComplexNumber(4, 5)
    b = ComplexNumber(2, 3)

    result_add = calc.add(a, b)
    print(f"Сложение: {result_add}")

    result_multiply = calc.multiply(a, b)
    print(f"Умножение: {result_multiply}")

    result_divide = calc.divide(a, b)
    print(f"Деление: {result_divide}")

if __name__ == "__main__":
    main()
