from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://dev321.seart.pl/")
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("SRIKTOR")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("passy")
# driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()