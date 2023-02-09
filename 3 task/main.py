import requests
from bs4 import BeautifulSoup
from colorama import Fore

url = "https://greenatom.ru/"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}


def get_count_tags(url: str, headers: dict) -> None:
    """Функция выводит в консоль количество его и количество тегов с атрибутами"""
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "lxml")

        tag_count = 0
        attribute_count = 0
        for tag in soup.descendants:
            tag_count += 1
            if hasattr(tag, 'attrs'):
                attribute_count += len(tag.attrs)

        print(Fore.GREEN + f"Общее количество вложенных HTML-тегов: {tag_count}")
        print(Fore.GREEN + f"Количество вложенных HTML-тегов, содержащих атрибуты: {attribute_count}")
    else:
        print(Fore.LIGHTRED_EX + f"Неверный запрос, статус код {response.status_code}")


if __name__ == "__main__":
    get_count_tags(url, headers)
