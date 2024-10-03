from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_selenium():
    options = Options()
    options.add_argument("--headless=old")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # Optional
    options.add_argument("--window-size=1920,1080")  # Optional, set a window size

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com')

    print(driver.title)  # Should print "Google" in the console
    driver.quit()

if __name__ == "__main__":
    test_selenium()