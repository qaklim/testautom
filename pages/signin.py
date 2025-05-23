from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser


class SignIn:

    def __init__(self, browser):
        self.browser = browser

    def check_title(self):
        title1 = self.browser.find_element(By.XPATH, "//h1[text()='Sign In']")
        return title1.is_displayed()

    def check_log_in(self, browser):
        email = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email.send_keys("test@foxportal.com")
        password = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
        )
        password.send_keys("123123123123")
        login_button = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()

    def click_sign_up(self, browser):
        signup = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Sign Up']"))
        )
        signup.click()