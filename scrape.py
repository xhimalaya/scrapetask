import requests
from bs4 import BeautifulSoup
import random
import json

def p_format(*args):
    ip_address, port, code, country, anonymity, google, https, last_checked = args
    return ip_address+":"+port

def ProxyDns():
    url = "https://free-proxy-list.net/"
    NUMBER_OF_ATTRIBUTES = 8
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    proxies = []
    table = soup.find('table')
    tbody = table.tbody if table else None

    if tbody:
        infos = tbody.find_all('tr')
        for info in infos:
            proxy_data_temp = [i.text for i in info]
            if len(proxy_data_temp) == NUMBER_OF_ATTRIBUTES:
                proxies.append(p_format(*proxy_data_temp))
        secure_random = random.SystemRandom()
        return secure_random.choice(proxies)

def scrapelocation(data):
    soup = BeautifulSoup(data)
    raw_json_data=json.loads(str(soup.find("script", {"id":"__NEXT_DATA__"})).replace('<script id="__NEXT_DATA__" type="application/json">','').replace("</script>",'').replace('\\u0026',','))
    for resturant_id, details in raw_json_data['props']["initialReduxState"]["pageRestaurantsV2"]["entities"]["restaurantList"].items():
        print("name >>>  ", details["name"])
        print("latitude >>>  ", details["latitude"])
        print("longitude >>>  ", details["longitude"])
        print("*"*60)