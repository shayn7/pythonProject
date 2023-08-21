from playwright.sync_api import Page

from pages.locators.main_page_locators import MainPageLocators
from pages.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.table_header = self.page.locator(MainPageLocators.TABLE_HEADER)
        self.text_box = self.page.locator(MainPageLocators.TEXT_BOX)
        self.table_rows = self.page.locator(MainPageLocators.TABLE_ROWS)
        self.add_button = self.page.locator(MainPageLocators.ADD_PERSON_BUTTON)
        self.column_headers = self.page.locator(MainPageLocators.COLUMN_HEADERS)

    def set_text(self, text):
        self.text_box.clear()
        self.text_box.fill(text)
        self.text_box.press("Enter")

    def click_on_add_person(self):
        self.add_button.click()

    def get_data_by_id(self, user_id, column_name):
        rows = self.table_rows
        column_headers = self.column_headers
        column_index = None
        index = 1

        while index <= column_headers.count():
            if column_headers.nth(index - 1).inner_text() == column_name:
                column_index = index

            index += 1

        data = rows.locator(":scope", has_text=user_id).locator(f"//td[{column_index}]")
        return data.inner_text()

    def get_all_data_for_a_column(self, column_name):
        column_index = None
        column_headers = self.column_headers
        index = 1

        while index <= column_headers.count():
            if column_headers.nth(index - 1).inner_text() == column_name:
                column_index = index

            index += 1

        column_data = self.page.locator(f"//table//tr//td[{column_index}]")
        return column_data.all_inner_texts()

    def get_all_users(self):
        rows = self.table_rows
        index = 1
        data = []
        while index < rows.count():
            data.insert(index, rows.nth(index).inner_text())
            index += 1

        return data
