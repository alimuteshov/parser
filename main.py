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
    url = "URL"
    headers = {
        "Accept": "SMTH",
        "User-Agent": "SMTH",
    }
    last_page_url = get_last_page_url(url)
    # last_page_number = int(last_page_url.split("=")[-1])
    last_page_number = 1
    logging.info("Starting links collection")

    # Iterating over website page numbers and collecting all news links
    for page_number in range(last_page_number + 1):
        logging.info(f"page_number = {page_number}")

        current_url = "".join(last_page_url.split("=")[:-1]) + "=" + f"{page_number}"

        req = requests.get(current_url, headers=headers)
        src = req.text

        soup = BeautifulSoup(src, "lxml")
        all_page_hrefs = soup.find_all("a", class_="list-media media")
        # Saving all pages links to txt file
        with open("all_page_hrefs.txt", "a") as file:

            for item in all_page_hrefs:
                item_href = item.get("href")
                file.write(f"{item_href}\n")

        time.sleep(random.randrange(2, 5))

        if page_number % 10 == 0 or page_number == 10:
            time.sleep(random.randrange(5, 9))

    # Creating csv file
    with open("data.csv", "w", encoding="utf-8") as file:
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

    with open("all_page_hrefs.txt", "r") as file:
        all_page_hrefs = file.readlines()

    all_page_hrefs = [page.strip() for page in all_page_hrefs]
    datestring = "%Y-%m-%d"
    logging.info("Starting info collection from links")
    # Iterating over all news linkconverting_to_datestrings
    for num, page_url in enumerate(all_page_hrefs[:1]):

        (
            title,
            pubdate,
            categories,
            atricle_body,
            tags,
            ext_links,
        ) = parse_info_from_pages(page_url, headers)

        # Filling csv file
        with open("data.csv", "a", encoding="utf-8") as file:
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
        time.sleep(random.randrange(2, 5))

        if num % 10 == 0 or num == 10:
            time.sleep(random.randrange(5, 9))


if __name__ == "__main__":
    main()
