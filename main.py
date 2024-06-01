

def main(input: str) -> str:
    symbols = input.split()

    if len(symbols) != 3:
        raise Exception('Формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)')

    s1, sign, s2 = symbols

    if float(s1) != int(float(s1)) or float(s2) != int(float(s2)):
        raise Exception('Числа не целые')

    s1, s2 = map(int, [s1, s2])

    if s1 < 1 or s1 > 10 or s2 < 1 or s2 > 10:
        raise Exception('Числа не могут быть меньше 1 и больше 10')

    if sign == '+':
        return str(int(s1) + int(s2))
    elif sign == '-':
        return str(int(s1) - int(s2))
    elif sign == '*':
        return str(int(s1) * int(s2))
    elif sign == '/':
        return str(int(s1) // int(s2))


while True:
    print(main(input()))