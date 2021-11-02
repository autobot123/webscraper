from selenium import webdriver

chromedriver_path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(chromedriver_path)

driver.get('https://scan.co.uk')

search_box_xpath = r'//*[@id="q"]'
components_button = r'//*[@id="mainMenu"]/div/div[2]/ul/li[2]/span'

search_box = driver.find_element_by_xpath(search_box_xpath)

search_box.send_keys('nvida gtx30')

