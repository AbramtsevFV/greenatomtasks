import requests
from bs4 import BeautifulSoup
page_url = 'https://greenatom.ru/'


def get_page(url: str) -> str:
    """Возвращает содержание страницы"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        with open('./page/index.html', 'w') as f:
            f.write(res.text)
    else:
        print(f"Ошибка подключения к {url}")

def get_tags(tag):
    print(tag)
    while tag:
        print(tag.findChildren)
        tag = tag.find_next()
        # print(tag, 888)
        # if tag.nex:
        #     print(tag.find('p'), 999)
def parsing_page():
    result = []
    with open('./page/index.html', 'r') as f:
        page = f.read()
    soup = BeautifulSoup(page, "lxml")
    tag_list = soup.find_all(recursive=True)
    print(tag_list)
    # for tag in tag_list[0]:
    #     result.append(tag.find_next())
    #     print(tag.findChildren())
    #     # get_tags(tag)


if __name__ == "__main__":
    # get_page(page_url)
    parsing_page()
