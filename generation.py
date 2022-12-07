# generation
from random import randint
from validation import ( 
    firstDigit,
    secondDigit
)

def listGenerator(n_cpfs):
    return [cpfGenerator() for i in range(0, n_cpfs)]

def digitsGenerator(cpf):
    first_digit = str(firstDigit(cpf))
    secondt_digit = str(secondDigit(cpf))
    return first_digit + secondt_digit

def cpfMask(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def cpfsMask(cpfs):
    return [cpfMask(cpf) for cpf in cpfs]

def cpfGenerator():
    cpf = ''.join([str(randint(0, 9)) for i in range(9)])
    return cpf + digitsGenerator(cpf)
