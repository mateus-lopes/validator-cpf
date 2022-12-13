# Mateus Lopes Albano -> https://github.com/mateus-lopes #
# ------------------------------------------------------ #
# --                GERADOR DE CPF                    -- #
# ------------------------------------------------------ #


# from colorama import Fore, Style
from os import system

from generation import (
    listGenerator,
    cpfsMask,
)

from validation import ( 
    cpfValidator,
)

# reusables
def formatText(text):
    print(f'\n{text}\n')

def formatList(object_list, count=1):
    text = ''
    for item in object_list:
        text += (f'{count} - {item}\n') if count else print(f'{item}')
        count += 1 
    return formatText(text) 

def formatInputBollean(content):
    validator = input(content)
    validator = 'y' if validator == '' else validator
    return True if validator == 'y' else False
    
def textColor(color, text):
    return color + text + Style.RESET_ALL


# interface
def generationInt():
    n_cpfs = int(input('\nhow many cpfs do you want: '))
    mask = formatInputBollean('With mask: [y/n] ( y ) ')
    cpfs = cpfsMask(listGenerator(n_cpfs)) if mask else listGenerator(n_cpfs)
    formatList(cpfs)
    return userInterface()

def validationInt():
    cpf = input('\nEnter your CPF: ')
    validator = cpfValidator(cpf)
    if validator:
        print('foi')
        # formatText(textColor(Fore.GREEN, '- Valid CPF -'))
    else:
        print('n foi')
        # formatText(textColor(Fore.RED, '- Invalid CPF -'))
    return userInterface()

def navInt(nav_list, input_message):
    nav_list = formatList(nav_list)
    while True:
        selection = input(input_message)
        if selection == '1':
            return generationInt()
        elif selection == '2':
            return validationInt()
        elif selection == '3':
            system('clear')
            return userInterface()
        elif selection == '4':
            return exit()
        else:
            print(textColor(Fore.LIGHTBLACK_EX, 'command not found'))       

def userInterface():
    formatText('------ CPF GENERATOR ------')    
    navInt(['Generate a CPF', 'Validate a CPF','Clear terminal', 'Exit'], 'select an option: ')


if __name__ == '__main__':
    userInterface()