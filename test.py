import requests
from bs4 import BeautifulSoup

# LicenseNumber, LicenseVersion, LastName, DateOfBirth

login_url = 'https://online.nzta.govt.nz/api/authentication'
#'https://online.nzta.govt.nz/licence-test/identification'

payload = {
    'LicenceNumber': 'ea050089',
    'LicenceVersion': '889',
    'LastName': 'wong',
    'DateOfBirth': '01-09-2001'
}

headers_ = {
    "Content-Type": "application/json"
}

r = requests.post(login_url, json=payload, headers=headers_)
print(r.text)
print(r.status_code)
# print(r.content)

# with requests.Session() as s:
#     p = s.post(login_url, data=payload)
#     print(p.text)
#     print(p.status_code)
#     print(p.content)
#
#     r = s.get('https://online.nzta.govt.nz/licence-test/booking/eligibility')
#     print(r.text)
