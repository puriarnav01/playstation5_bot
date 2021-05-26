from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pywhatkit
from twilio.rest import Client
import time
import argparse


def reach_reliance_digital(client, product, pin, email, password, BANK, CARD_NUMBER, NAME_ON_CARD, MONTH, YEAR, CVV, phone):
    print("opening product page")
    browser  = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(product)
    time.sleep(7)
    
    print("opened product page")
    print("adding to cart")
    try:
        browser.find_element_by_id("RIL_PDPInputPincode").send_keys(pin)
        time.sleep(3)
        browser.find_element_by_id("buy_now_main_btn").click()
        time.sleep(5)
    except Exception as e:
        print("not added to cart")
        browser.close()
        return None
    print("added to cart")
    print("loggin in")
    try:
        browser.find_element_by_id("email").send_keys(email)
        browser.find_element_by_id("pass").send_keys(password)
        time.sleep(3)
    
        browser.find_element_by_xpath("//div[@class='sc-chPdSV eWorQt']//div[@class='sc-chPdSV gTZViT']//div[@class='sc-chPdSV cfMmfZ']//div[@class='sc-chPdSV iesTLv']//button[@class='ripple sc-bwzfXH ePDJxz sc-jzJRlG dDDLqU']").click()
        time.sleep(20)
    except Exception as e:
        print("login failed")
        browser.close()
        return None
    print('logged in')
    print('entering bank details')
    try:
        print('entered payment portal')
        browser.find_element_by_id("select-emi-bank").send_keys(BANK)


        browser.find_element_by_id('c-number-CC').send_keys(CARD_NUMBER)
        browser.find_element_by_id('c-name-CC').send_keys(NAME_ON_CARD)
        browser.find_element_by_id('c-exprmm-CC').send_keys(MONTH)
        browser.find_element_by_id('c-expryy-CC').send_keys(YEAR)
        browser.find_element_by_id('c-cvv-CC').send_keys(CVV)
        time.sleep(3)
        client.messages.create(body='Hi your bot has reached ps5 razor pay gateway, please open the browser asap',
                               from_='+14702883714',
                               to= '+91' + phone)
        while True:
            print("payment entered for ps5.. stay here")
            time.sleep(10)
    except Exception as e:
        print("failed entering portal")
        browser.close()
    return None