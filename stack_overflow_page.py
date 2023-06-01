import os,logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

def login():
    logging.info("Logging into stackoverflow.com")

    driver = webdriver.Chrome()
    try:
        driver.get("https://stackoverflow.com")

        driver.find_element("link text", "Log in").click()

        driver.find_element("id", "email").send_keys(os.environ['STACK_OVERFLOW_EMAIL'])
        driver.find_element("id", "password").send_keys(os.environ['STACK_OVERFLOW_PASSWORD'])
        driver.find_element("id", "submit-button").submit()

        driver.find_element(By.PARTIAL_LINK_TEXT, os.environ.get('STACK_OVERFLOW_DISPLAY_NAME')).click()

        elem = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.ID, "js-daily-access-calendar-container"))
        )
        logging.info("Logged into stackoverflow.com and accessed profile page - " + elem.text)

    except Exception as e:
        print("An error occurred while trying to access stackoverflow.com!", e)
    finally:
        driver.close()


if __name__ == "__main__":
    login()
