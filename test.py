import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By

payload = {
    'LicenceNumber': '-',
    'LicenceVersion': '-',
    'LastName': '-',
    'DateOfBirth': '-',
}

headers_ = {
    "Content-Type": "application/json"
}

available_times = []

login_url = 'https://online.nzta.govt.nz/licence-test/identification'

opts = webdriver.ChromeOptions()
opts.headless = True
driver = Chrome(options=opts)

assert opts.headless
browser = Chrome(options=opts)
browser.get(login_url)

# Login Info
time.sleep(2)
licence_number = browser.find_element(by=By.XPATH, value="//input[@formcontrolname='LicenceNumber']")
licence_version = browser.find_element(by=By.XPATH, value="//input[@formcontrolname='LicenceVersion']")
last_name = browser.find_element(by=By.XPATH, value="//input[@formcontrolname='LastName']")
date_of_birth = browser.find_element(by=By.XPATH, value="//input[@formcontrolname='DateOfBirth']")

# Login
licence_number.send_keys(payload.get('LicenceNumber') + Keys.TAB + payload.get('LicenceVersion') + Keys.TAB + payload.get('LastName') + Keys.TAB + payload.get('DateOfBirth') + Keys.ENTER)

# Click Reschedule
time.sleep(5)
(browser.find_element(by=By.ID, value="btnContinue")).click()

# Click Location
time.sleep(3)
(browser.find_element(by=By.XPATH, value="//*[contains(text(), '-')]")).click()
(browser.find_element(by=By.XPATH, value="//*[contains(text(), '-')]")).click()
(browser.find_element(by=By.XPATH, value="//*[contains(text(), '-')]")).click()


input("Press ENTER to exit\n")

# while True:
#     pass


# print(browser.text)
# browser.close()
# quit()

# r = requests.post(login_url, json=payload, headers=headers_)
# print(r.text)
# print(r.status_code)

# print(r.content)

# with requests.Session() as s:
#     p = s.post(login_url, data=payload)
#     print(p.text)
#     print(p.status_code)
#     print(p.content)
#
#     r = s.get('https://online.nzta.govt.nz/licence-test/booking/eligibility')
#     print(r.text)
