import requests
from bs4 import BeautifulSoup

payload = {
    'LicenseNumber': '...',
    'LicenseVersion': '...',
    'LastName': '...',
    'DateOfBirth': '...'
}

with requests.Session() as s:
    p = s.post('https://online.nzta.govt.nz/licence-test/identification', data=payload)
    print(p.text)

    r = s.get('https://online.nzta.govt.nz/licence-test/booking/eligibility')
    print(r.text)
