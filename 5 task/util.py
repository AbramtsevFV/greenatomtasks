from typing import Optional

import regex_spm
from colorama import Fore


def compare(version_a: list, version_b: list) -> int:
    """Сравнение """
    if version_a[0] < version_b[0]:
        return -1
    if version_a[0] == version_b[0] and version_a[1] < version_b[1]:
        return -1
    if version_a[0] == version_b[0] and version_a[1] == version_b[1]:
        return 0
    return 1

def check(version: str) -> bool:
    """Проверка входных данных"""

    match regex_spm.fullmatch_in(version):
        case r"(\d+)\.(\d+)":
            return True
        case _:
            return False


def compare_versions(version_a: str, version_b: str) -> Optional[int]:
    """Функция сравнения версий
        На вход поступает строка вида: 2.10
    """
    if check(version_a) and check(version_b):
        versions_parser = lambda x: list(map(int, str(x).split('.')))
        version_a = versions_parser(version_a)
        version_b = versions_parser(version_b)

        print(compare(version_a, version_b))
    else:
        print(Fore.LIGHTRED_EX + 'Неверный формат входных данных')


