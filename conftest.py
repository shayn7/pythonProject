import pytest
from playwright.sync_api import Page
from pages.page_objects.main_page import MainPage
from pages.page_objects.add_new_member_page import AddNewMemberPage
from slugify import slugify
from pathlib import Path


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


@pytest.mark.hookwrapper(scope='session', autouse=True)
def pytest_runtest_makereport(item, call) -> None:
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if call.when == "call":
        if call.excinfo is not None and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path(".playwright-screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            filename = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=filename)
            if filename:
                html = '<div><img src="%s" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % filename
                extra.append(pytest_html.extras.html(html))
    report.extra = extra
