from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pywhatkit
from twilio.rest import Client
import time
import argparse


def reach_checkout_sony_center(client, product_url, product_id, email,
                               first_name, last_name, address, number, city,
                               country, state, phone, pin_code):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(product_url)
    time.sleep(10)
    try:
        print("checking pin code")
        browser.find_element_by_id("pincode_input").send_keys(pin_code)
        time.sleep(3)
        browser.find_element_by_id("check-delivery-submit").click()
        print("moving towards checkout")
        time.sleep(3)
    except Exception as e:
        print(e)
        browser.close()
    if browser.find_element_by_class_name(
            "check-pincode-msg").text == 'This PIN code is serviceable.':
        print("your pin code is servicable")
        try:
            print("adding to cart")
            browser.find_element_by_xpath(
                "//div[@class='{}']//input[@id='product-add-to-cart']".format(
                    product_id)).click()
            print("added to cart")
            time.sleep(7)
            print("viewing cart")
            browser.find_element_by_xpath(
                "//div[@class='actions']//a[@class='btn btn-view-cart']").click()
            print("done viewing cart")
            time.sleep(7)
            print("proceeding to checkout")
            browser.find_element_by_id("checkout_button").click()
            print("done with checkout")
            time.sleep(7)
            print("entering details")
            browser.find_element_by_name('checkout[email]').send_keys(email)
            browser.find_element_by_name(
                'checkout[shipping_address][first_name]').send_keys(first_name)
            browser.find_element_by_name(
                'checkout[shipping_address][last_name]').send_keys(last_name)
            browser.find_element_by_name(
                'checkout[shipping_address][address1]').send_keys(address)
            browser.find_element_by_name(
                'checkout[shipping_address][address2]').send_keys(number)
            browser.find_element_by_name(
                'checkout[shipping_address][city]').send_keys(city)
            browser.find_element_by_id(
                'checkout_shipping_address_country').send_keys(country)
            browser.find_element_by_id(
                'checkout_shipping_address_province').send_keys(state)
            browser.find_element_by_id(
                'checkout_shipping_address_phone').send_keys(phone)
            time.sleep(5)
            print("entered details")
            browser.find_element_by_id('continue_button').click()
            print("past continue 1")
            time.sleep(12)
            browser.find_element_by_id('continue_button').click()
            print("past continue 2")
            time.sleep(12)
            browser.find_element_by_id('continue_button').click()
            print("past continue 3")
            time.sleep(12)
        except Exception as e:
            print(e)
            browser.close()

        if browser.find_element_by_xpath(
                "//div[@class='razorpay-container']//div[@class='razorpay-backdrop']"):
            print("reached razorpay gateway")
            client.messages.create(
                body='Hi your bot has reached ps5 razor pay gateway, please open the browser asap',
                from_='+14702883714',
                to='+91' + phone)
            while browser.find_element_by_xpath(
                    "//div[@class='razorpay-container']//div[@class='razorpay-backdrop']"):
                print("holding here")
                time.sleep(10)
        else:
            print("couldnt reach, trying again in the next iteration")
            browser.close()
    else:
        print("your pin is not servicable, try a different pin")
        browser.close()

    return 1
