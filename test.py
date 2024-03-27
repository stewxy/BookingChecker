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

# Check Calender
for i in range(4):
    table = browser.find_element(by=By.TAG_NAME, value="tbody")
    for row in table.find_elements(by=By.XPATH, value=".//tr"):
        available_times += [td.text for td in row.find_elements(by=By.XPATH, value=".//td[@class!='ui-state-disabled']") if td.text != ""]
    print(available_times)
    time.sleep(1)
    (browser.find_element(by=By.CLASS_NAME, value="ui-datepicker-next")).click()

if len(available_times) == 0:
    print("No Available Times")
else:
    print(available_times)

# td = browser.find_elements(by=By.TAG_NAME, value="td")
# for x in td:
#     # print('$', x.get_attribute('outerHTML'), '$')
#     if x.find_element(by=By.XPATH, value="//td[@class='ui-state-disabled']"):
#         available_times.append(x.text)
# print(list(filter(None, available_times)))


while True:
    pass
