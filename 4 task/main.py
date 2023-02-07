from utils import get_ip
from colorama import Fore

"""Получение публичного IP компьютера"""


def main():
    """Запуск скрипта для получения IP"""
    res = get_ip()
    if res:
        print(Fore.GREEN + f'Ваш IP: {res}')
    else:
        print(Fore.LIGHTRED_EX + 'Неверный запрос')


if __name__ == '__main__':
    main()
