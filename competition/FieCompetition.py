from selenium.webdriver.common.by import By
from collections import Counter

from .Competition import Competition
from knas_worldranking import knas_worldranking


class FieCompetition(Competition):
    def __init__(self, url):
        super().__init__(url)  # Call the parent constructor
        self.reroute()
        self.name = self.extract_name()
        self.extract_variables()


    def reroute(self):
        self.url = self.url.replace("competitions", "competition")
        self.url += "/entry/pdf?lang=en"


    def extract_name(self):
        self.driver.get(self.url)
        name = self.driver.find_element(By.XPATH, "/html/body/div/h2").get_attribute("textContent")
        return name

    
    def extract_variables(self):

        competitor_elements = self.driver.find_elements(By.CLASS_NAME, "col1.col-no-wrap") 
        competitors = [competitor_element.get_attribute("textContent").strip() for competitor_element in competitor_elements]
        country_elements = self.driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr/td[2]") 
        countries = [country.get_attribute("textContent").strip() for country in country_elements]
        
        self.sum_x = 0
        for competitor in competitors:
            if competitor in knas_worldranking:
                self.sum_x += knas_worldranking[competitor][0]
        print(F"sum_x: ", self.sum_x)

        self.n = len(competitors)
        print(F"n: ", self.n)


        country_counter = Counter(countries)
        self.p = min(7, sum(1 for count in country_counter.values() if count > 2))
        print(F"p: ", self.p)