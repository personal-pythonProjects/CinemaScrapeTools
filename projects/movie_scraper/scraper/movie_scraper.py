import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from projects.movie_scraper.scraper.base_scraper import BaseScraper
from projects.movie_scraper.utils.settings import BASE_URL, OUTPUT_FOLDER, ENDPOINT


class MovieScraper(BaseScraper):

    def __init__(self, base_url = BASE_URL, endpoint = ENDPOINT, output_folder = OUTPUT_FOLDER):
        super().__init__(base_url, endpoint, output_folder)

    def fetch_data(self, page):
        url = f"{self.base_url + self.endpoint}?page={page}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to fetch data from page {page}")

    def parse_data(self, raw_html):
        soup = BeautifulSoup(raw_html, 'lxml')
        movies_list = soup.select("ul.scripts-list li")

        movies_data = []

        for movie in movies_list:
            title_tag = movie.find("a")
            if title_tag:
                title = title_tag.text.strip()
                link = f"https://subslikescript.com{title_tag['href']}"
                year = title.split('(')[1].replace(')', '') if '(' in title else 'Unknown'
                movies_data.append({"Title": title, "Link": link, "Year": year})

        return movies_data

    def save_to_csv(self, data, filename):
        output_path = os.path.join(self.output_folder, filename)
        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False)
