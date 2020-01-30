from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

searchItem = "Amd Ryzen 3900X"
sites = ["https://www.1a.ee/", "https://www.arvutitark.ee/", "https://www.galador.ee/"]
timeBetweenRequests = 10

def searchGalador():
    inputElement = browser.find_element_by_xpath('//*[@id="top-info-container"]/div/div[1]/div[1]/form/div/input')
    inputElement.send_keys(searchItem)
    inputElement.send_keys(Keys.ENTER)
    xPath = '//*[@id="product-listing"]/div[1]/a/div[4]'
    try:
        print("Galadoris toote hind: " + browser.find_elements_by_xpath(xPath)[0].text)
    except IndexError:
        print("Toode puudub Galadoris.")

def searchArvutitark():
    inputElement = browser.find_element_by_xpath('//*[@id="search-products"]')
    inputElement.send_keys(searchItem)
    inputElement.send_keys(Keys.ENTER)
    xPath = '/html/body/div[3]/div[1]/section/section[4]/div/div/div/div[2]/ul/li[1]/div/div[2]/div[2]/div[2]/span[2]'
    time.sleep(1)
    try:
        print("Arvutitargas toote hind: " + browser.find_elements_by_xpath(xPath)[0].text)
    except IndexError:
        print("Toode puudub")
def search1a():
    inputElement = browser.find_element_by_xpath('//*[@id="q"]')
    inputElement.send_keys(searchItem)
    inputElement.send_keys(Keys.ENTER)
    xPath = '/html/body/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[3]/div[2]/div/div/div[1]/div/span/span[1]'
    time.sleep(1)
    try:
        print("1a-s toote hind: " + browser.find_elements_by_xpath(xPath)[0].text + " €")
    except IndexError:
        print("Toode puudub")
browser = webdriver.Chrome()
while True:
    browser.get(sites[0])
    search1a()
    browser.get(sites[1])
    searchArvutitark()
    browser.get(sites[2])
    searchGalador()
    time.sleep(timeBetweenRequests)