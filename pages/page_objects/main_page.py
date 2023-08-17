from playwright.sync_api import Page

from pages.locators.main_page_locators import MainPageLocators
from pages.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.table_header = self.page.locator(MainPageLocators.TABLE_HEADER)
        self.text_box = self.page.locator(MainPageLocators.TEXT_BOX)
        self.table_body = self.page.locator(MainPageLocators.TABLE_BODY)
        self.add_button = self.page.locator(MainPageLocators.ADD_PERSON_BUTTON)

    def set_text(self, text):
        self.text_box.clear()
        self.text_box.fill(text)
        self.text_box.press("Enter")

    def click_on_add_person(self):
        self.add_button.click()

    def get_users_on_page(self):
        rows = self.table_body
        index = 0
        data = []
        while index < rows.count():
            # print(rows.nth(index).inner_text())
            data.insert(index, rows.nth(index).inner_text())
            index += 1

        return '.'.join(str(x) for x in data)
