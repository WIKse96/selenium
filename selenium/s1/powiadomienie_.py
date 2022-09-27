import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestNotifi(unittest.TestCase):

    def setUp(self):
        self.serviceObj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serviceObj)
        self.driver.get('https://vu2005.admin.s37.mhost.eu/')
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.assertIn("Akcesoria, uchwyty, okucia meblowe - RustykalneUchwyty.pl", self.driver.title)

    def test_OpenSimpleProduct(self):
        self.actions = ActionChains(self.driver)
        self.menuRoot = self.driver.find_element(By.CSS_SELECTOR,
                                                 "body > div:nth-child(6) > div:nth-child(2) > div:nth-child(6) > div:nth-child(5) > div:nth-child(3) > nav:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
        self.menuFirstLvl = self.driver.find_element(By.CSS_SELECTOR,
                                                     "body > div:nth-child(6) > div:nth-child(2) > div:nth-child(6) > div:nth-child(5) > div:nth-child(3) > nav:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)")
        self.actions.move_to_element(self.menuRoot).perform()
        self.actions.click(self.menuFirstLvl).perform()

        # do przerobienia
        self.productCards = self.driver.find_elements(By.XPATH,
                                                      "//body/div[@class='wrapper']/div[@class='page']/div[@class='main-container container col2-left-layout']/div[@class='main row']/div[@class='col-main col-sm-9 col-md-9']/div[@class='category-products']/ul[@class='products-grid column3 row first last odd']/li")
        assert self.driver.find_element(By.XPATH,
                                        "//a[@title='Drzwi przesuwne drewniane dębowe MarX']"), "Produkt znaleziono"

        self.driver.find_element(By.XPATH, "//a[@title='Drzwi przesuwne drewniane dębowe MarX']").click()
        #
        # assert self.driver.find_element(By.XPATH, "//input[@value='Powiadom o dostępności']")
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".product-shop.col-sm-7"), "OK")
        self.btnNotify = self.driver.find_element(By.CSS_SELECTOR, "input[value='Powiadom o dostępności']")
        # testuj bez uzupełnienia danych
        time.sleep(3)
        self.btnNotify.click()
        self.notificationMsg = self.driver.find_element(By.CSS_SELECTOR, "#notyfication-message")
        self.assertTrue("Nie udało się zapisać adresu email. Adres email jest nieprawidłowy" in self.notificationMsg.text)
        self.driver.refresh()
        #z niepoprawnym email
        self.btnNotify = self.driver.find_element(By.CSS_SELECTOR, "input[value='Powiadom o dostępności']")
        self.notificationInput = self.driver.find_element(By.CSS_SELECTOR, "#email-notification")
        self.notificationInput.send_keys("email.com")
        self.btnNotify.click()
        self.notificationMsg = self.driver.find_element(By.CSS_SELECTOR, "#notyfication-message")
        self.assertTrue("Nie udało się zapisać adresu email. Adres email jest nieprawidłowy" in self.notificationMsg.text)
        self.driver.refresh()
        #z niepoprawnymi danymi
        self.btnNotify = self.driver.find_element(By.CSS_SELECTOR, "input[value='Powiadom o dostępności']")
        self.notificationInput = self.driver.find_element(By.CSS_SELECTOR, "#email-notification")
        self.notificationInput.send_keys("email@")
        self.btnNotify.click()
        self.notificationMsg = self.driver.find_element(By.CSS_SELECTOR, "#notyfication-message")
        self.assertTrue("Nie udało się zapisać adresu email. Adres email jest nieprawidłowy" in self.notificationMsg.text)
        self.driver.refresh()

    def test_Testowy(self):
        self.driver.minimize_window()
        print("test_testowy")
        time.sleep(5)




    def tearDown(self):
        time.sleep(1)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
