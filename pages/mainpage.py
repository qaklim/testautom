from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, browser):
        self.browser = browser

    def open (self):
        self.browser.get("https://rewasd.com")

    def click_about (self):
        about = self.browser.find_element(By.XPATH, "//a[text()='About']")
        about.click()

    def find_about(self):
        about = self.browser.find_element(By.XPATH, "//a[text()='About']")
        return about

    def find_why_to_use(self):
        why_to_use = self.browser.find_element(By.XPATH, "//a[text()='Why to Use']")
        return why_to_use

    def click_why_to_use(self):
        why_to_use = self.browser.find_element(By.XPATH, "//a[text()='Why to Use']")
        why_to_use.click()

    def find_dropdown_why_to_use(self):
        dropdown_how_it_works = self.browser.find_element(By.XPATH, "//div[text()='How It Works']")
        return dropdown_how_it_works

    def find_button_buy_now_on_header(self):
        button = self.browser.find_element(By.XPATH, "//a[text()='Buy Now']")
        return button

    def find_button_download_on_header(self):
        button = self.browser.find_element(By.XPATH, "//div[@title='Download']")
        return button

    def click_button_download_on_header(self):
        button = self.browser.find_element(By.XPATH, "//div[@title='Download']")
        button.click()

    def check_download_on_header_is_opening_dropdown(self):
        items = [
            self.browser.find_element(By.XPATH, "//a[text()='Download']"),
            self.browser.find_element(By.XPATH, "//a[text()='Download for ARM']")
        ]
        return items

    def click_on_dropdown_items_download_on_header_x64(self):
        x64 = self.browser.find_element(By.XPATH, "//a[text()='Download']")
        x64.click()

    def click_on_dropdown_items_download_on_header_arm(self):
        arm = self.browser.find_element(By.XPATH, "//a[text()='Download']")
        arm.click()

    def click_on_sign_in(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Sign In']")))
        sign = self.browser.find_element(By.XPATH, "//a[contains(@class, 'btn-navbar') and @aria-label='Sign In']")
        sign.click()
