from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, base_url, endpoint, output_folder):
        self.base_url = base_url
        self.endpoint = endpoint
        self.output_folder = output_folder

    @abstractmethod
    def fetch_data(self, page):
        pass

    @abstractmethod
    def parse_data(self, raw_html):
        pass
