import pytest
from playwright.sync_api import Page
from pages.page_objects.main_page import MainPage


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