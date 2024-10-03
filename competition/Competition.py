from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from abc import ABC, abstractmethod
from formulas import P_formula

import time


class Competition(ABC):
    def __init__(self, url):
        self.url = url
        self.driver = self.initiate_session()

    @abstractmethod
    def extract_name(self):
        pass

    def initiate_session(self):
        options = Options()
        options.add_argument("--headless=old")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")  # Optional for Windows systems
        driver = webdriver.Chrome(options=options) 
        return driver

    def calculate_percentage(self):
        percentage = P_formula(self.sum_x, self.n, self.p)
        print(f"percentage: {percentage}%")
        return percentage





