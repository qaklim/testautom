import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class SignUp:
    def __init__(self, browser):
        self.browser = browser

    def check_sign_up_title(self):
        title = self.browser.find_element(By.XPATH, "//h1[text()='Sign Up']")
        return title

    def fill_email(self, browser):
        max_attempts = 3  # Максимальное количество попыток для обхода stale
        for attempt in range(max_attempts):
            try:
                # Ожидаем кликабельный элемент
                email = WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
                )
                email.clear()
                test_email = self.generate_email
                print(f"Попытка {attempt + 1}: Ввод email: {test_email}")
                # Устанавливаем значение через JavaScript
                browser.execute_script("arguments[0].value = arguments[1];", email, test_email)
                browser.execute_script("arguments[0].dispatchEvent(new Event('input'));", email)
                browser.execute_script("arguments[0].dispatchEvent(new Event('change'));", email)
                # Проверяем значение
                print(f"После ввода через JS: {email.get_attribute('value')}")
                # Ожидаем, что значение сохранилось
                WebDriverWait(browser, 5).until(
                    lambda driver: driver.find_element(By.XPATH, "//input[@type='email']").get_attribute(
                        "value") == test_email
                )
                print(f"После ожидания: {email.get_attribute('value')}")
                # Проверяем ошибки валидации
                try:
                    error = WebDriverWait(browser, 2).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "//div[contains(@class, 'error') or contains(text(), 'email')]"))
                    )
                    print(f"Ошибка валидации: {error.text}")
                except TimeoutException:
                    print("Ошибок валидации не найдено")
                return  # Успешно, выходим из цикла
            except StaleElementReferenceException as e:
                print(f"StaleElementReferenceException на попытке {attempt + 1}: {str(e)}")
                if attempt == max_attempts - 1:
                    raise Exception("Не удалось заполнить email после нескольких попыток")
                time.sleep(0.5)  # Пауза перед повторной попыткой
            except TimeoutException as e:
                print(f"TimeoutException при ожидании значения email: {str(e)}")
                raise
    @property
    def generate_email(self, random_number=None):
        timestamp = time.strftime("%H%M%S")
        random_number = str(random.randint(1, 99999))
        return f"{timestamp}{random_number}test@autotestqa.com"

    def fill_password(self, browser):
        password = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password' and @aria-label='Password']"))
        )
        password.send_keys("123123123123")
        time.sleep(0.5)
        repeat_password = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password' and @aria-label='Repeat password']"))
        )
        repeat_password.send_keys("123123123123")
        time.sleep(1)

    def click_register(self, browser):
        register = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        register.click()

    def check_sign_up_is_done_successful(self, browser):
        success_title = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space(text())='Thank you']"))
        )
        success_title2 = WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='for Signing Up']"))
        )
        return success_title.is_displayed() and success_title2.is_displayed()
