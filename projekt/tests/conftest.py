import pytest
from selenium.webdriver.chrome import webdriver

#oznaczenie, że poniższa funkcja jest w scope klasy
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path='E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe')
    driver.get("https:/rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    #zadeklarowanie driver w taki sposób aby przekazać go do innego pliku
    request.cls.driver = driver
    #tutaj wykonują się testy, yield to oznacza
    yield
    #po wszystkim na koniec przegladarka się zamyka
    driver.close()
