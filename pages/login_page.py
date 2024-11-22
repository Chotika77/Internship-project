from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class LoginPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[id='email-2']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[id='field']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")
    PAGE_BODY = (By.CSS_SELECTOR, '.login-body')  # LOCATOR


    def log_in(self):
        sleep(2)
        self.wait_to_be_clickable(*self.EMAIL_FIELD)
        self.input_text('d.chkuaseli@yahoo.com', *self.EMAIL_FIELD)
        sleep(2)
        self.wait_to_be_clickable(*self.PASSWORD_FIELD)
        self.input_text('Sereli1977', *self.PASSWORD_FIELD)
        actions = ActionChains(self.driver)
        reely_page = self.find_element(*self.PAGE_BODY)
        actions.move_to_element(reely_page).click().perform()
        sleep(2)
        self.wait_to_be_clickable_click(*self.CONTINUE_BUTTON)
        # sleep(5)

