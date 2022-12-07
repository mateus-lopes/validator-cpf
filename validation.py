# validation
def equalNumbers(numbers):
    return numbers == numbers[::-1]

def digitsCalc(cpf, numbers_length):
    digit, x = 0, 0
    while x < numbers_length:
        digit += int(cpf[x]) * x
        x += 1
    return digitsCalcTwo(digit)

def digitsCalcTwo(digit):
    digit %= 11
    return 0 if digit == 10 else digit 

def firstDigit(cpf): 
    return digitsCalc(cpf, 8)

def secondDigit(cpf):
    return digitsCalc(cpf, 9)

def cpfLength(cpf):
    return len(cpf) == 11

def verifyDigits(first_digit, second_digit, cpf):
    return first_digit == int(cpf[-2]) and second_digit == int(cpf[-1])

def cpfValidator(cpf):
    if cpfLength(cpf):
        first_digit = firstDigit(cpf)
        secondt_digit = secondDigit(cpf)
        return (not equalNumbers(cpf)) and verifyDigits(first_digit, secondt_digit, cpf)
    return False