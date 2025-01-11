from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from formulas import percentage_formula


class Competition():
    def __init__(self, url):
        self.url = url
        print(f"url: {self.url}")
        self.driver = self.initiate_session()


    def initiate_session(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")  # Optional for Windows systems
        driver = webdriver.Chrome(options=options)
        return driver


    def calculate_percentage(self):
        percentage = percentage_formula(self.sum_x, self.n, self.p)
        return percentage






