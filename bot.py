import datetime, time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

DELAY = 5 # seconds


def run_on_page(url, title_validation_token):
    driver.get(url)
    if title_validation_token:
        assert "GIGABYTE" in driver.title
    elem = driver.find_element(By.ID, "ProductBuy")
    if not 'out of stock' in elem.text.lower():
        elem.click()
    else:
        print(f"Out of Stock Found @ {datetime.datetime.now()}/r")
    

if __name__ == "__main__":
    driver = webdriver.Firefox()

    print("Press CTRL+C to End")
    count = 0
    failed = 0
    success = 0
    last_attempt = None
    last_success = None
    while True:
        last_attempt = datetime.datetime.now()
        count += 1
        page_result = run_on_page(
            'https://www.newegg.com/gigabyte-gv-n5090gaming-oc-32gd-nvidia-geforce-rtx-5090-32gb-gddr7/p/N82E16814932761',
            'GIGABYTE'
        )
        if page_result:
            success += 1
            last_success = datetime.datetime.now()
        print(f"Attempted {count} times (last attempt: {last_attempt}). {failed}/{count} failures (last success: {last_success})./r")
        time.sleep(DELAY)
    # driver.close() # should be called if not using CTRL+C