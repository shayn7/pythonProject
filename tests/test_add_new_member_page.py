from playwright.sync_api import expect
from pages.page_objects.add_new_member_page import AddNewMemberPage
from pages.page_objects.main_page import MainPage


def test_add_new_member(main_page: MainPage, add_new_member_page: AddNewMemberPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.click_on_add_person()
    expect(add_new_member_page.add_new_member_window).to_be_visible()
    add_new_member_page.add_new_user("george", "costenza")
    main_page.set_text("14")
    actual_users = main_page.get_users_on_page()
    assert actual_users.__contains__("costenza")