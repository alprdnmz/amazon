from selenium import webdriver
import pages.finding_locators
from pages.POM import Login
from pages.POM2 import Search
from pages.POM3 import List
import time


def amazon_login():

    # task no 2 : open login page and enter user credentials

    userlogin = Login(driver)
    userlogin.enter_mail("alperdonmez0226@gmail.com")
    userlogin.click_continue()
    userlogin.enter_password("Kazak26!")
    userlogin.click_signin()


def search_box():

    # task no 3 : Enter "samsung" on the search box

    samsungsearch = Search(driver)
    samsungsearch.search_text("samsung")
    pages.finding_locators.click_by_xpath(driver, "//div[@class='nav-search-submit nav-sprite']//input[@class='nav-input']")


def search_results():

    # task no 4 : Approve search results is for "samsung"

    time.sleep(2)
    result = driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold']")
    print(result)
    assert result.text == '"samsung"'


def second_page():

    # task no 5 : Click 2nd page and approve you are on the 2nd page

    pages.finding_locators.click_by_xpath(driver, "//li[@class='a-normal']//a[contains(text(),'2')]")
    page_number = driver.find_element_by_xpath("//li[@class='a-selected']//a[contains(text(),'2')]")
    assert page_number.text == "2"


def pick_product():

    # task no 6 : Select the 3rd product on the 2nd page and add it to List

    productselection = List(driver)
    pages.finding_locators.click_by_xpath(driver, "//span[@class='celwidget slot=SEARCH_RESULTS template=SEARCH_RESULTS widgetId=search-results index=2']//img[@class='s-image']")
    time.sleep(2)
    productselection.click_wishlist()
    time.sleep(3)
    productselection.click_wishlist_withproduct()
    time.sleep(2)
    selected_product = driver.find_element_by_xpath("//li[2]//table[1]//tbody[1]//tr[1]//td[1]")
    name = selected_product.text
    pages.finding_locators.click_by_xpath(driver, "//span[contains(text(),'Continue shopping')]")
    time.sleep(2)

    return name

def list_view(selected_product_name):

    # task no 7 : Click list and open wish list

    pages.finding_locators.click_by_xpath(driver, "//a[@id='nav-link-accountList']")
    time.sleep(2)
    pages.finding_locators.click_by_xpath(driver, "//a[contains(text(),'Manage your lists')]")
    time.sleep(2)
    pages.finding_locators.click_by_ID(driver, "wl-list-title-1IA0UU0PQ7XH2")

    # task no 8 : Confirm that the product on the list is same product which is selected on the pick_product function

    on_the_list_product = driver.find_element_by_xpath("//h3[@class='a-size-base']")
    assert selected_product_name == on_the_list_product.text

    # task no 9 : Click delete button for the product

    time.sleep(2)
    driver.find_element_by_name("submit.deleteItem").click()
    time.sleep(3)
    driver.refresh()
    time.sleep(5)

    # task no 10 : Confirm the product is deleted on the list

    list_items = driver.find_element_by_xpath("//span[@class='a-size-medium a-color-base']")

    assert list_items.text == "0 items in this view", "There are products on the wish list"



if __name__ == '__main__':

    # task no 1 : open amazon.com and assert you are on the home page

    driver = webdriver.Chrome("C:/Users/alper/PycharmProjects/chromedriver_win32/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    assert driver.title == "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more", "You are not in home page"

    pages.finding_locators.click_by_xpath(driver, "//a[@id='nav-link-accountList']")

    amazon_login()
    time.sleep(3)
    search_box()
    search_results()
    second_page()
    selected_product_name = pick_product()
    list_view(selected_product_name)


