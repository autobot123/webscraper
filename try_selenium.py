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
        EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
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

# store as json?
gpu_list_id = {}
gpu_list_id['rtx 3060 ti'] = 6
gpu_list_id['rtx 3070 ti'] = 5

for gpu, list_id in gpu_list_id.items():
    tickbox_xpath = f'//*[@id="gpu_filter"]/div/div/div/ul/li[{list_id}]/div/label'
    gpu_tickbox = get_element_by_xpath(driver, tickbox_xpath)
    gpu_tickbox.click()

nvidia_manufacturer_button_xpath = '//*[@id="manufacturer_filter"]/div/div/div/ul/li[1]/div/label'
manufacturer_tickbox = get_element_by_xpath(driver, nvidia_manufacturer_button_xpath)
manufacturer_tickbox.click()

buy_btns = get_element_proper_by_class_name(driver, 'featured-buy-link')

for btn in buy_btns:
    if btn.text != 'OUT OF STOCK':
        print(f"gpu is not out of stock")
    elif btn.txt == 'OUT OF STOCK':
        print(f"button text = {btn.text}")
