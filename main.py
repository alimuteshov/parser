import requests
from bs4 import BeautifulSoup
import time
import random
import csv
import logging
import os
from utils import get_last_page_url, parse_info_from_pages


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


def main():
    url = "https://www.aceee.org/news"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
    }

    last_page_url = get_last_page_url(url, headers=headers)

    last_page_number = int(last_page_url.split("=")[-1])

    logging.info("Starting links collection")

    # Iterating over website page numbers and collecting all news links
    for page_number in range(last_page_number + 1):
        logging.info(f"page_number = {page_number}")

        current_url = (
            url + "".join(last_page_url.split("=")[:-1]) + "=" + f"{page_number}"
        )

        req = requests.get(current_url, headers=headers)
        src = req.text

        soup = BeautifulSoup(src, "lxml")
        all_page_hrefs = soup.find_all("a", class_="list-media media")
        # Saving all pages links to txt file
        with open("data/all_page_hrefs.txt", "a") as file:

            for item in all_page_hrefs:
                item_href = item.get("href")
                file.write(f"{item_href}\n")

        # time.sleep(random.randrange(2, 5))

        if page_number % 15 == 0:
            time.sleep(random.randrange(5, 7))

    # Creating csv file
    with open("data/data.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "title",
                "pubdate",
                "datestring",
                "categories",
                "article_body",
                "tags",
                "external_links",
            )
        )

    with open("data/all_page_hrefs.txt", "r") as file:
        all_page_hrefs = file.readlines()

    all_page_hrefs = [page.strip() for page in all_page_hrefs]
    datestring = "%Y-%m-%d"
    logging.info("Starting info collection from links")
    # Iterating over all news linkconverting_to_datestrings
    for num, page_url in enumerate(all_page_hrefs):

        (
            title,
            pubdate,
            categories,
            atricle_body,
            tags,
            ext_links,
        ) = parse_info_from_pages(page_url, headers)

        # Filling csv file
        with open("data/data.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    pubdate,
                    datestring,
                    categories,
                    atricle_body,
                    tags,
                    ext_links,
                )
            )
        logging.info(f"link number = {num}")
        # time.sleep(random.randrange(1, 2))

        if num % 100 == 0 or num == 10:
            time.sleep(random.randrange(5, 9))


if __name__ == "__main__":
    main()
