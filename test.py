import time
from selenium import webdriver
from selenium.webdriver import Keys, ChromeOptions
from selenium.webdriver.common.by import By

payload = {
    "LicenceNumber": "-",
    "LicenceVersion": "-",
    "LastName": "-",
    "DateOfBirth": "-",
}

available_times = []

login_url = "https://online.nzta.govt.nz/licence-test/identification"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"

options = ChromeOptions()
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--headless=new")
options.add_argument("--window-size=1920x1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

browser = webdriver.Chrome(options=options)
browser.get(login_url)

# Fill Login Info
print("Logging In...")
time.sleep(2)
licence_number = browser.find_element(by=By.XPATH, value="//input[@formcontrolname='LicenceNumber']")
licence_number.send_keys(payload.get("LicenceNumber") + Keys.TAB + payload.get("LicenceVersion") + Keys.TAB + payload.get("LastName") + Keys.TAB + payload.get("DateOfBirth") + Keys.ENTER)

# Click Reschedule
print("Waiting for Login...")
time.sleep(5)
(browser.find_element(by=By.ID, value="btnContinue")).click()

# Select Booking Location
print("Selecting booking location...")
time.sleep(3)
(browser.find_element(by=By.XPATH, value="//*[contains(text(), '-')]")).click()
(browser.find_element(by=By.XPATH, value="//*[contains(text(), '-')]")).click()
(browser.find_element(by=By.XPATH, value="//*[contains(text(), '-')]")).click()

# Check Calender
print("Checking for available booking slots...")
for i in range(4):
    table = browser.find_element(by=By.TAG_NAME, value="tbody")
    for row in table.find_elements(by=By.XPATH, value=".//tr"):
        month = browser.find_element(by=By.CLASS_NAME, value="ui-datepicker-title")
        available_times += [[month.text, td.text] for td in row.find_elements(by=By.XPATH, value=".//td[@class!='ui-state-disabled']") if td.text != ""]
    time.sleep(1)
    (browser.find_element(by=By.CLASS_NAME, value="ui-datepicker-next")).click()

# Show Available Time Slots
if len(available_times) == 0:
    print("No Available Slots")
else:
    for item in available_times:
        print("== Available Slots == \n" + item[1], item[0] + "\n")
