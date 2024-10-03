from selenium import webdriver


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
        driver = webdriver.Chrome()
        return driver

    def calculate_percentage(self):
        percentage = P_formula(self.sum_x, self.n, self.p)
        print(f"percentage: {percentage}%")
        return percentage





