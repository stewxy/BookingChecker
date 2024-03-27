import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

test_links = results.find_all("a")
print(test_links, "***")

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    links = job_element.find_all("a")

    apply_link = [link for link in links if link["href"] !="https://www.realpython.com"]
    print("Apply here:", apply_link[0]["href"],  "\n")

    # link_url = job_element.find_all("a")[1]["href"]
