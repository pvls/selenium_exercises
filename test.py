import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

MAIN_URL = "https://google.com/"
GITHUB = "github"

class MyTests:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_access_github_through_google(self):
        try:
            self.driver.get(MAIN_URL)
        except TimeoutException:
            print ("Timed out")

        self.driver.maximize_window()
        self.driver.find_element(By.NAME, "q").send_keys(GITHUB, Keys.ENTER)
        self.driver.find_element(By.CLASS_NAME, "VuuXrf").click()
        assert True
        time.sleep(2)
        self.driver.close()

    def test_find_breed(self):
        self.driver.get("https://seleniumplayground.practiceprobs.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.CLASS_NAME, "md-search__input").send_keys("Breed", Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Akita Inu')]").click()
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    runner = MyTests()git
    # runner.test_access_github_through_google()
    runner.test_find_breed()