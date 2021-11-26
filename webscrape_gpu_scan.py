from webscraper import Webscraper

def webscrape_gpu_scan():
    webscraper = Webscraper(set_headless=True)

    nvidia_store_url = r'https://store.nvidia.com/en-gb/geforce/store/'
    webscraper.driver.get(nvidia_store_url)
    webscraper.sleep_random()

    gpu_list_id = {}
    gpu_list_id['rtx 3060 ti'] = 6
    gpu_list_id['rtx 3070 ti'] = 5

    for gpu, list_id in gpu_list_id.items():
        tickbox_xpath = f'//*[@id="gpu_filter"]/div/div/div/ul/li[{list_id}]/div/label'
        gpu_tickbox = webscraper.get_element_by_xpath(webscraper.driver, tickbox_xpath)
        gpu_tickbox.click()

    nvidia_manufacturer_button_xpath = '//*[@id="manufacturer_filter"]/div/div/div/ul/li[1]/div/label'
    manufacturer_tickbox = webscraper.get_element_by_xpath(webscraper.driver, nvidia_manufacturer_button_xpath)
    manufacturer_tickbox.click()

    buy_btns = webscraper.get_element_proper_by_class_name(webscraper.driver, 'featured-buy-link')

    for btn in buy_btns:
        if btn.text != 'OUT OF STOCK':
            print(f"gpu is not out of stock")
        elif btn.text == 'OUT OF STOCK':
            print(f"button text = {btn.text}")


if __name__ == "__main__":
    webscrape_gpu_scan()
