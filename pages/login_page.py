from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        
        login_url = self.browser.current_url
        assert  login_url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/", "Ссылка вверная"
        assert True

    def should_be_login_form(self):
        
        assert self.is_element_present(*LoginPageLocators.form_of_login), "Есть форма логина"
        assert True

    def should_be_register_form(self):
        
        assert self.is_element_present(*LoginPageLocators.For_of_regist), "Есть форма регистрации"
        assert True