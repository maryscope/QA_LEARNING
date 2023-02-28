import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("connect_driver")
@allure.suite("Тест на логин. Практика")
class TestLogin:

    LOGIN = "Hflkig@fr!-1"
    PASSWORD = "Hflkig@fr!-1"
    URL_LOGIN = "https://demoqa.com/login"

    LOGIN_FIELD = ("xpath","//input[@id='userName']")
    PASSWORD_FIELD = ("xpath","//input[@id='password']")
    LOGIN_BUTTON = ("xpath","//button[@id='login']")

    @allure.title("Логин в аккаунт")
    @allure.description("Зайти в аккаунт и сделать скриншот")
    @allure.severity("Critical")
    @pytest.mark.login
    def test_login_in_account(self):
        with allure.step("Открыть страницу"):
            self.driver.get("https://demoqa.com/login")

        with allure.step("Ввод Логина"):
            self.driver.find_element(*self.LOGIN_FIELD).send_keys(self.LOGIN)

        with allure.step("Ввод ароля"):
            self.driver.find_element(*self.PASSWORD_FIELD).send_keys(self.PASSWORD)

        with allure.step("Нажатие на кнопку"):
            self.driver.find_element(*self.LOGIN_BUTTON).click()
            self.wait.until(EC.url_to_be("https://demoqa.com/profile"))

        with allure.step("Проверка авторизации успешна"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Скриншот1", attachment_type=AttachmentType.PNG)



