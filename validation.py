# validation
def equalNumbers(numbers):
    return numbers == numbers[::-1]

def cleanCpf(cpf):
    return ''.join([x for x in cpf if x.isdigit()])

def digitOne(cpf):
    digit, x = 0, 1
    for c in cpf:
        digit += int(c) * (x)
        x += 1
    return digitsCalc(digit)

def digitTwo(cpf):
    digit, x = 0, 0
    for c in cpf:
        digit += int(c) * x
        x += 1
    return digitsCalc(digit)

def digitsCalc(digit):
    digit %= 11
    return 0 if digit == 10 else digit 

def firstDigit(cpf): 
    return digitOne(cpf[:9])

def secondDigit(cpf):
    return digitTwo(cpf[:10])

def cpfLength(cpf):
    return len(cpf) == 11

def verifyDigits(first_digit, second_digit, cpf):
    return first_digit == int(cpf[-2]) and second_digit == int(cpf[-1])

def cpfValidator(cpf):
    cpf = cleanCpf(cpf)
    if cpfLength(cpf):
        first_digit = firstDigit(cpf)
        second_digit = secondDigit(cpf)
        return (not equalNumbers(cpf)) and verifyDigits(first_digit, second_digit, cpf)
    return False