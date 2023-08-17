from playwright.sync_api import Page


class BasePage:
    URL: str

    def __init__(self, page: Page) -> None:
        self.locator = None
        self.page = page

    def go_to_page(self) -> None:
        self.page.goto(self.URL)

    def strip_white_space(self, value):
        return value.replace(" ", "").replace("\t", "").replace("\n", "")

    def reload_page(self):
        self.page.reload()

