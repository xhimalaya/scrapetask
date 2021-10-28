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
    soup = BeautifulSoup(data, features="html.parser")
    all_div_tab = soup.find_all("div", {"class": "ant-col-24 RestaurantListCol___1FZ8V ant-col-md-12 ant-col-lg-6"})
    print(">>>>>>  <<<<<<< ", len(all_div_tab))
    for url_soup in all_div_tab:
        resturent_url="https://food.grab.com/"+(url_soup.find("a")["href"])
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        resturant_source = requests.get(resturent_url, headers=headers)
        sub_soup = BeautifulSoup(resturant_source.text, features="html.parser")
        raw_json_data=json.loads(str(sub_soup.find("script", {"id":"__NEXT_DATA__"})).replace('<script id="__NEXT_DATA__" type="application/json">','').replace("</script>",'').replace('\\u0026',','))
        geo_data = raw_json_data['props']["initialReduxState"]["geolocation"]["currentLocation"]
        print("latitude >> ", geo_data["latitude"])
        print("longitude >> ", geo_data["longitude"])
        print("name >>>>  ", sub_soup.find("h1",{"class":"name___1Ls94"}).text)
        print("_"*60)