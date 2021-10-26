from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.proxy import Proxy, ProxyType
import scrape
import os

# Set PRoxy
print("Setting the proxy")
proxy_ip_port  = scrape.ProxyDns()
proxy = Proxy({
  'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_ip_port,
    'ftpProxy': proxy_ip_port,
    'sslProxy': proxy_ip_port,
    'noProxy': ''
})
print(" Using Proxy ", proxy_ip_port)

driver = webdriver.Firefox(executable_path=os.path.join(os.getcwd(),"geckodriver.exe"), proxy=proxy)
try:
    driver.get("https://food.grab.com/ph/en/")
    time.sleep(5)
    insert_address = driver.find_element_by_xpath('//*[@id="location-input"]')
    print("<><><>>>>>>  ", insert_address)
    insert_address.send_keys("Philippines")
    time.sleep(2)
    insert_address.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath('//button[@class="ant-btn submitBtn___2roqB ant-btn-primary"]').click()
    time.sleep(2)
    while True:
        try:
            driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-block"]').click()
            scrape.scrapelocation(driver.page_source)
        except Exception as e:
            print("I think all page load is completed", e)
            break
        time.sleep(1)
except Exception:
    pass
driver.quit()