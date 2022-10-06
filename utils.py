import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from typing import Dict, List, Tuple


def get_last_page_url(url: str) -> str:
    """Takes a link to the main page and returns the link of the last page."""
    service = Service("YOUR_PATH")
    driver = webdriver.Chrome(service=service)

    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(
        By.XPATH,
        "//button[@class='decline-button eu-cookie-compliance-secondary-button button clear inverted']",
    ).click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@title='Go to last page']").click()
    time.sleep(6)
    current_url = driver.current_url
    driver.close()
    driver.quit()

    return current_url


def parse_info_from_pages(
    page_url: str, headers: Dict[str, str]
) -> Tuple[str, str, str, str, str, List[str]]:
    """Takes a page link and header file and return needed information from page"""
    req = requests.get("https://www.aceee.org" + page_url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    title = soup.find("div", class_="hero-text").find("h1").text
    pubdate = (
        soup.find("div", class_="hero-text").find("div", class_="summary").text.strip()
    )
    categories = page_url.split("/")[1]

    atricle_body = soup.find(
        "div", class_="small-6 small-offset-2 medium-5 medium-offset-1 cell"
    ).text

    if len(atricle_body.split("This Article Was About")) == 2:
        atricle_body, tags = (
            atricle_body.split("This Article Was About")[0],
            atricle_body.split("This Article Was About")[-1],
        )
    else:
        tags = "None"

    ext_links = []
    for link in soup.find(
        "div", class_="small-6 small-offset-2 medium-5 medium-offset-1 cell"
    ).findAll("a", href=True):
        ext_links.append(link.get("href"))

    return (
        title.strip(),
        converting_to_datestring(pubdate.strip()),
        categories,
        atricle_body.strip(),
        tags.strip(),
        ext_links,
    )


def converting_to_datestring(datestring: str) -> str:
    """Converts date to right format"""
    given_format = "%B %d, %Y"
    date = datetime.strptime(datestring, given_format)

    return str(date).split()[0]
