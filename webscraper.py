from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randint
from typing import Type


class Webscraper:
    def __init__(self, set_headless: bool = False, chromedriver_path: str = "C:\Program Files (x86)\chromedriver.exe") -> None:
        self.chromedriver_path = chromedriver_path
        self.driver = self.create_webdriver(set_headless = set_headless)

    def create_webdriver(self, set_headless: bool) -> Type[webdriver.chrome.webdriver.WebDriver]:
        print("Creating driver")
        chrome_options = webdriver.ChromeOptions()
        if set_headless:
            print("Running in headless mode")
            chrome_options.add_argument('--headless')
        else:
            print("Running in interactive mode")
        return  webdriver.Chrome(self.chromedriver_path, options=chrome_options)

    def sleep_random(self, min: int=1, max: int=5) -> None:
        duration = randint(min,max)
        print(f"Sleeping for {duration} seconds")
        sleep(duration)

    def get_element_by_xpath(self, driver: webdriver, xpath: str, timeout: int=10) -> Type[webdriver.remote.webelement.WebElement]:
        self.sleep_random()
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    def get_element_proper_by_class_name(self, driver: webdriver, class_name: str, timeout: int=10) -> Type[webdriver.remote.webelement.WebElement]:
        self.sleep_random()
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        return element
