import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup") - dziedziczone z BaseClass
class TestOne(BaseClass):

    def test_e2e(self, setup):

        self.driver.find_element(By.CLASS_NAME, "a[href*='shop']").click()
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        i = 1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)

            if cardText == "Blackberry":
                self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()

