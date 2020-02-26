from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

def click_by_xpath(driver, path):
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        element.click()
    except TimeoutException:
        element = None
    return element


def click_by_ID(driver, path):
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, path)))
        element.click()
    except TimeoutException:
        element = None
    return element

if __name__ == "__main__":
    click_by_xpath()
    click_by_ID()