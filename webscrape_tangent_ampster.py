from webscraper import Webscraper

def main():
    webscraper = Webscraper(set_headless=True)

    richer_sounds_url = r'https://www.richersounds.com/tangent-ampster-bt-mkii.html'
    webscraper.driver.get(richer_sounds_url)
    webscraper.sleep_random()

    accept_cookes_xpath = r'//*[@id="onetrust-accept-btn-handler"]'
    accept_cookies = webscraper.get_element_by_xpath(webscraper.driver, accept_cookes_xpath)
    accept_cookies.click()

    tangent_ampster_price_xpath = r'//*[@id="product-price-17099"]/span'
    prices = webscraper.get_element_proper_by_class_name(webscraper.driver, 'price')
    tangent_ampster_price = prices[1]
    print(f"tangent ampster bt ii price = {tangent_ampster_price.text}")


if __name__ == "__main__":
    main()
