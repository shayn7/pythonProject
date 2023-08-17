import pytest
from playwright.sync_api import Page
from pages.page_objects.main_page import MainPage
from pages.page_objects.add_new_member_page import AddNewMemberPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }


@pytest.fixture()
def main_page(page: Page):
    return MainPage(page)

@pytest.fixture()
def add_new_member_page(page: Page):
    return AddNewMemberPage(page)