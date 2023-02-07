from utils import get_ip
from colorama import Fore


def main():
    res = get_ip()
    if res:
        print(Fore.GREEN + f'Ваш IP: {res}')
    else:
        print(Fore.LIGHTRED_EX + 'Неверный запрос')


if __name__ == '__main__':
    main()
