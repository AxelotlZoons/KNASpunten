import regex as re
import time
from selenium.webdriver.common.by import By
from collections import Counter

from .Competition import Competition
from knas_worldranking import knas_worldranking


class FieCompetition(Competition):
    def __init__(self, url):
        super().__init__(url)  # Call the parent constructor
        self.check_url()

        # self.name = self.extract_name()
        # print(f"Name: {self.name}")

        self.determine_state()

        self.extract_variables()


    def check_url(self):
        correct_url_format = r"https:\/\/fie\.org\/competitions\/\d{4}\/\d*"
        match = re.fullmatch(correct_url_format, self.url)

        if not match:
            print(f"The url seems incorrect: {self.url}")
            return

    def redirect_to_entries(self):

        self.url = self.url.replace("competitions", "competition")
        self.url += "/entry/pdf?lang=en"
        self.driver.get(self.url)

    def redirect_to_results(self):

        results_tab_element = self.driver.find_element(By.ID, "results")
        self.driver.execute_script("arguments[0].click();", results_tab_element)


    # def extract_name(self):
    #     self.driver.get(self.url)
    #     name = self.driver.find_element(By.XPATH, "/html/body/div/h2").get_attribute("textContent")
    #     return name


    def determine_state(self):
        self.driver.get(self.url)
        results_tab_elements = self.driver.find_elements(By.XPATH, "//*[@id='results']")
        print(F"results_tab_elements: {results_tab_elements}")
        if len(results_tab_elements) != 0:
            self.state = "post"
        else:
            self.state = "pre"

        print(f"state: {self.state}")


    def extract_variables(self):

        match self.state:
            case "pre":
                self.redirect_to_entries()
                competitors, countries = self.extract_variables_pre_comp()
            case "post":
                self.redirect_to_results()
                competitors, countries = self.extract_variables_post_comp()

        self.sum_x = 0
        for competitor in competitors:
            if competitor in knas_worldranking:
                self.sum_x += knas_worldranking[competitor][0]

        self.n = len(competitors)

        country_counter = Counter(countries)
        self.p = min(7, sum(1 for count in country_counter.values() if count > 2))


    def extract_variables_pre_comp(self):
        competitor_elements = self.driver.find_elements(By.CLASS_NAME, "col1.col-no-wrap")
        competitors = [competitor_element.get_attribute("textContent").strip() for competitor_element in competitor_elements]
        country_elements = self.driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr/td[2]")
        countries = [country.get_attribute("textContent").strip() for country in country_elements]

        return competitors, countries


    def extract_variables_post_comp(self):

        pages = len(self.driver.find_elements(By.XPATH, '(//*[@class="pager"])[1]/li')) - 2

        competitors = []
        countries = []
        for page in range(0, pages):
            competitor_elements = self.driver.find_elements(By.XPATH, '//*[@class="Grid RankingGrid"]/div/div/table/tbody/tr/td[3]/a')
            country_elements = self.driver.find_elements(By.XPATH, '//*[@class="Grid RankingGrid"]/div/div/table/tbody/tr/td[5]/a')
            rank_elements = self.driver.find_elements(By.XPATH, '//*[@class="Grid RankingGrid"]/div/div/table/tbody/tr/td[1]/a')

            for competitor_element, country_element, rank_element in zip(competitor_elements, country_elements, rank_elements):

                if rank_element.get_attribute('textContent') != '9999':
                    competitors.append(competitor_element.get_attribute('textContent'))
                    countries.append(country_element.text)

            time.sleep(5)
            next_page_button = self.driver.find_elements(By.XPATH, '//*[@class="pager"]/li/a')[-1]
            self.driver.execute_script("arguments[0].click();", next_page_button)

        return competitors, countries
