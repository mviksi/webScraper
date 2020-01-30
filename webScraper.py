from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.auto24.ee/kasutatud/nimekiri.php?bn=2&a=101&aj=&ae=1&af=50&ag=0&ag=1&otsi=otsi')

cars = []
carPrices = []



def auto24():
    xPath1 = '//*[@id="usedVehiclesSearchResult"]/tbody/tr['
    xPath2 = ']/td[2]/a'
    for i in range(1,5):
        print("testing i:" + str(i))
        xPath = xPath1 + str(i) + xPath2
        car = browser.find_elements_by_xpath(xPath)[0].text
        cars.append(car)
def printAuto24Info():
    print(cars[0])
    print(cars[1])
    print(cars[2])
    print(cars[3])
auto24()
printAuto24Info()
browser.close()