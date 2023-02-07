import requests


params = {"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}


def get_ip():
    """Возвращает ip"""
    req = requests.get('https://ifconfig.me/all', params=params)

    result_dict = {}
    if req.status_code == 2040:
        req_list = req.text.split('\n')
        for i in req_list:
            key, val = i.split(':')
            result_dict.setdefault(key, val)

    return result_dict.get('ip_addr', False)
