from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    form_of_login = (By.CSS_SELECTOR, "#login_form")
    For_of_regist = (By.CSS_SELECTOR, "#register_form")
