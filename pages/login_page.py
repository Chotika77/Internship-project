from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class LoginPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[id='email-2']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[id='field']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")



    def log_in(self):
        sleep(2)
        self.wait_to_be_clickable(*self.EMAIL_FIELD)
        self.input_text('d.chkuaseli@yahoo.com', *self.EMAIL_FIELD)
        sleep(2)
        self.wait_to_be_clickable(*self.PASSWORD_FIELD)
        self.input_text('Sereli1977', *self.PASSWORD_FIELD)
        sleep(2)
        self.wait_to_be_clickable_click(*self.CONTINUE_BUTTON)
        # sleep(5)

