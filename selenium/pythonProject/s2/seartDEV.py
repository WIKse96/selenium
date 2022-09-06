from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

loginData = {
    "id": 1,
    "loginEmail": "wiktor.cwiertnia.seart@gmail.com",
    "loginPass": "Test123*",
    "nickName": "wiktor TEST!"
}

service_obj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://dev321.seart.pl/")
driver.find_element(By.XPATH,"//a[@title='Zaloguj']").click()

loginPath = driver.current_url

driver.find_element(By.ID, "email").send_keys(loginData["loginEmail"].replace(' ', ''))
driver.find_element(By.ID, "pass").send_keys(loginData["loginPass"].replace(' ', ''))

driver.find_element(By.ID, "send2").click()
if loginPath == driver.current_url:
    print("Błędne hasło lub login")
    print(f"email:{loginData['loginEmail']}")
    print(f"hasło:{loginData['loginPass']}")
elif "https://dev321.seart.pl/customer/account/" == driver.current_url:
    print("Dostęp przyznany - zalogowano")
    print(driver.current_url)
    message = driver.find_element(By.CLASS_NAME, "welcome-msg").text
else:
    print("cos jest źle")

assert f"{loginData['nickName']}" in message

# driver.close()