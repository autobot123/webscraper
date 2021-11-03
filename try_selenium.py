from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randint



def sleep_random(min: int=1, max: int=5):
    duration = randint(min,max)
    print(f"Sleeping for {duration} seconds")
    sleep(duration)


def get_element_by_xpath(driver: webdriver, xpath: str, timeout: int=10):
    sleep_random()
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return element

def get_element_proper_by_class_name(driver: webdriver, class_name: str, timeout: int=10):
    sleep_random()
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CLASS_NAME, class_name))
    )
    return element

### SCRIPT ###
set_headless = False

chrome_options = webdriver.ChromeOptions()
if set_headless:
    chrome_options.add_argument('--headless')

chromedriver_path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(chromedriver_path, options=chrome_options)

nvidia_store_url = r'https://store.nvidia.com/en-gb/geforce/store/'
driver.get(nvidia_store_url)
sleep_random()
rtx_3060_ti_tickbox_xpath = '//*[@id="gpu_filter"]/div/div/div/ul/li[6]/div/label'
gpu_tickbox = get_element_by_xpath(driver, rtx_3060_ti_tickbox_xpath)
gpu_tickbox.click()

nvidia_manufacturer_button_xpath = '//*[@id="manufacturer_filter"]/div/div/div/ul/li[1]/div/label'
manufacturer_tickbox = get_element_by_xpath(driver, nvidia_manufacturer_button_xpath)
manufacturer_tickbox.click()

buy_btns = [get_element_proper_by_class_name(driver, 'featured-buy-link')]

for btn in buy_btns:
    if btn.text != 'OUT OF STOCK':
        print(f"gpu in stock")

