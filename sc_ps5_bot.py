from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pywhatkit
from twilio.rest import Client
import time
import argparse
from helper.reliance_digital import reach_reliance_digital
from helper.sony_center import reach_checkout_sony_center

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-st", "--store", required=True, help="store selector")
    ap.add_argument("-to", "--token", required=True, help="twilio token")
    ap.add_argument("-pr", "--product", required=True, help="product url")
    ap.add_argument("-pid", "--pro_id", required=True, help="product_id")
    ap.add_argument("-e", "--email", required=True, help="email id")
    ap.add_argument("-pa", "--pword", required=True, help="password")
    ap.add_argument("-f", "--fname", required=True, help="first name")
    ap.add_argument("-l", "--lname", required=True, help="last name")
    ap.add_argument("-a", "--address", required=True, help="address")
    ap.add_argument("-ap", "--apart", required=True, help="apart")
    ap.add_argument("-c", "--city", required=True, help="city")
    ap.add_argument("-co", "--country", required=True, help="country")
    ap.add_argument("-s", "--state", required=True, help="state")
    ap.add_argument("-p", "--phone", required=True, help="phone")
    ap.add_argument("-pi", "--pin", required=True, help="pin")
    ap.add_argument("-ba", "--bank", required=True, help="bank")
    ap.add_argument("-ca", "--card", required=True, help="card number")
    ap.add_argument("-cn", "--cname", required=True, help="name on card")
    ap.add_argument("-mo", "--month", required=True, help="Month")
    ap.add_argument("-y", "--year", required=True, help="year")
    ap.add_argument("-cv", "--cvv", required=True, help="cvv")

    args = vars(ap.parse_args())

    account = "AC567a9c4f67727815a87b4369943afa6a"
    token = args['token']
    client = Client(account, token)
    if args['store'] == 's':
        reach_checkout_sony_center(client, args['product'], args['pro_id'],
                                   args['email'], args['fname'], args['lname'],
                                   args['address'], args['apart'],
                                   args['city'], args['country'],
                                   args['state'], args['phone'],
                                   args['pin'])
    elif args['store'] == 'r':
        reach_reliance_digital(client, args['product'], args['pin'], args['email'],
                               args['pword'],
                               args['bank'], args['card'], args['cname'],
                               args['month'], args['year'], args['cvv'],
                               args['phone'])
