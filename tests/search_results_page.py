from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    RUSSIAN_TEXT = (By.XPATH,"//h1[@class='h1-menu' and text()='Главное меню']")


    # def verify_results(self):
    #     self.verify_text("Главное меню", *self.RUSSIAN_TEXT)

    def verify_results(self):
        self.wait_for_element_to_appear(*self.RUSSIAN_TEXT)
        message = self.find_element(*self.RUSSIAN_TEXT).text
        print(message)


