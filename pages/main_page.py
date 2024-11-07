from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import Page

class MainPage(Page):
    # EN_ICON = (By.CSS_SELECTOR, "#w-dropdown-toggle-0")
    # EN_ICON = (By.ID, "#w-dropdown-toggle-0")
    EN_ICON = (By.XPATH, "//div[@id='w-dropdown-toggle-0']")
    # EN_ICON = (By.CSS_SELECTOR, '[lang="en"]')
    # CLICK_MAIN_MENU = (By.XPATH, "//a[@href='/main-menu' and @aria-current='page']")
    CLICK_MAIN_MENU = (By.XPATH, '//a[@href="/main-menu" and contains(@class, "menu-button-block")]')
    RU_ICON = (By.CSS_SELECTOR, '[lang="ru"]')




    def open_main(self):
        self.open('https://soft.reelly.io/')
        sleep(3)

    def click_main_menu(self):
        sleep(5)
        self.wait_to_be_clickable_click(*self.CLICK_MAIN_MENU)
        sleep(3)

    def change_language(self):
        sleep(3)
        en_icon = self.find_element(*self.EN_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(en_icon)
        actions.perform()
        ru_button = self.find_element(*self.RU_ICON)
        actions.move_to_element(ru_button).click().perform()






