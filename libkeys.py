import time
import unittest

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestKeys(unittest.TestCase):

    USERNAME = (By.ID, "username")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.implicitly_wait(1)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_keys(self):
        user = self.driver.find_element(*self.USERNAME)
        user.send_keys("tomsmith")
        time.sleep(2)
        user.clear()
        user.send_keys("tomsmith")
        time.sleep(1)
        user.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        user.send_keys("tomsmith")
        time.sleep(1)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(1)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(1)
        user.send_keys(Keys.ARROW_LEFT)
        pass

