import random
import os
import time

os.system('pip install colorama')
os.system('cls')

import colorama
from colorama import Fore, Back, Style
colorama.init (autoreset=True)

print('')
print('')
print('')

print(f'{Fore.BLUE}|||||         |||||    |||||     |||||           |||||')
print(f'{Fore.RED}|||||      ||||||      |||||     |||||           |||||')
print(f'{Fore.BLUE}|||||    ||||||        |||||     |||||           |||||')
print(f'{Fore.RED}|||||  |||||           |||||     |||||           |||||')
print(f'{Fore.BLUE}|||||||||              |||||     |||||           |||||')
print(f'{Fore.RED}|||||  |||||           |||||     |||||           |||||')
print(f'{Fore.BLUE}|||||    ||||||        |||||     |||||           |||||')
print(f'{Fore.RED}|||||      ||||||      |||||     |||||           |||||')
print(f'{Fore.BLUE}|||||         |||||    |||||     ||||||||||||    ||||||||||||')
print('Password Generator By Valerio Gamba, Windows Edition')

print('')
print('')
print('')

time.sleep(1.5)

print(f'{Fore.CYAN}Le seguenti informazioni non saranno usate per completare la password, sono solo a scopo informativo...')

print('')
print('')
print('')

time.sleep(1.5)

nome = input(f'{Fore.CYAN}inserisci il tuo nome: ')

time.sleep(0.5)

cognome = input(f'{Fore.CYAN}inserisci il tuo cognome: ')

time.sleep(0.5)

localize = input(f'{Fore.CYAN}di dove sei?: ')

time.sleep(0.5)

sex = input(f'{Fore.CYAN}Sesso(M - F): ')

time.sleep(1.5)

print('')
print('')

if sex == 'M': 
    print(f'{Fore.BLUE}Benvenuto signor',nome,cognome,'      Cominciamo')
elif sex == 'F':
    print(f'{Fore.MAGENTA}Benvenuta signora',nome,cognome,'     Cominciamo')

print('')
time.sleep(0.5)

print('')
print('')
print('')

passlen = int(input(f"{Fore.CYAN}Inserisci la lunghezza desisderata per la password (8-21): "))

print('')
print('')


char ="ABCDEFGHILMNOPQRSTUVZ.abcdefghilmnopqrstuvz1234567890"
p = "".join(random.sample(char,passlen ))

print(f'{Fore.CYAN}Generazione password...')

time.sleep(3)

print(f'{Fore.CYAN}operazione completata..., ecco la tua password ')


print('')
print('')

time.sleep(0.5)

print(p)

print('')
print('')
print(f'{Fore.RED}Ora copiala e non condividerla con nessuno!')
print('')

input('')