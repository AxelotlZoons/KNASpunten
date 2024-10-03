from selenium.webdriver.common.by import By
from collections import Counter

from .Competition import Competition
from knas_worldranking import knas_worldranking


class FtlCompetition(Competition):
    def __init__(self, url):
        super().__init__(url)  # Call the parent constructor
        self.name = self.extract_name()
        print(self.name)
        self.extract_variables()


    def extract_name(self):
        self.driver.get(self.url)
        name = self.driver.find_element(By.CLASS_NAME, "desktop.tournName").get_attribute("textContent")
        return name

    
    def extract_variables(self):

        competitor_elements = self.driver.find_elements(By.XPATH, "//*[@id='resultList']/tbody/tr/td[2]") 
        competitors = [competitor_element.get_attribute("textContent").strip() for competitor_element in competitor_elements]
        country_elements = self.driver.find_elements(By.XPATH, "//*[@id='resultList']/tbody/tr/td[3]") 
        countries = [country.get_attribute("textContent").strip() for country in country_elements]
        
        self.sum_x = 0
        for competitor in competitors:
            if competitor in knas_worldranking:
                self.sum_x += knas_worldranking[competitor][0]
        print(self.sum_x)

        self.n = len(competitors)
        print(self.n)


        country_counter = Counter(countries)
        self.p = min(7, sum(1 for count in country_counter.values() if count > 2))
        print(self.p)