from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class MakeOrder:
    def __init__(self, websiteToTest, productToOrder):
        self.websiteToTest = websiteToTest
        self.productToOrder = productToOrder

        self.serviceObj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serviceObj)

    def makeOrder(self):
        self.driver.get(self.websiteToTest)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "//input[@name='q']").send_keys(self.productToOrder)


obj = MakeOrder('https://dev321.seart.pl/customer/account/', 'łóżko')
obj.makeOrder()