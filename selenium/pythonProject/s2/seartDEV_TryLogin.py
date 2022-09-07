from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TryLogin:

    def __init__(self, idUser, loginEmail, loginPass, nickName, websiteToTest, accountUrl):

        self.id = idUser
        self.loginEmail = loginEmail
        self.loginPass = loginPass
        self.nickName = nickName
        self.websiteToTest = websiteToTest
        self.accountUrl = accountUrl
        self.serviceObj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
        self.loginPath = ''
        self.message = None

    def login(self):

        driver = webdriver.Chrome(service=self.serviceObj)
        driver.get(self.websiteToTest)
        driver.find_element(By.XPATH, "//a[@title='Zaloguj']").click()

        self.loginPath = driver.current_url

        driver.find_element(By.ID, "email").send_keys(self.loginEmail)
        driver.find_element(By.ID, "pass").send_keys(self.loginPass)

        driver.find_element(By.ID, "send2").click()
        if self.loginPath == driver.current_url:
            print("Błędne hasło lub login")
            print(f"email:{self.loginEmail}")
            print(f"hasło:{self.loginPass}")
        elif self.accountUrl == driver.current_url:
            print("Dostęp przyznany - zalogowano")
            print(f"użytkownik: {self.loginEmail}")
            print(driver.current_url)
            self.message = driver.find_element(By.CLASS_NAME, "welcome-msg").text
        else:
            print("cos jest źle")

        assert f"{self.nickName}" in self.message
        driver.close()


