from playwright.sync_api import Page
from pages.locators.add_new_members_locators import AddNewMemberPageLocators
from pages.page_objects.base_page import BasePage


class AddNewMemberPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.add_new_member_window = self.page.locator(AddNewMemberPageLocators.ADD_NEW_MEMBER_WINDOW)

    def add_new_user(self, name, family):
        self.page.get_by_label("Name").fill(name)
        self.page.get_by_label("Family").fill(family)
        self.page.get_by_role("button", name="Add").click()


