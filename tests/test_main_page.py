from playwright.sync_api import expect

from pages.page_objects.main_page import MainPage


def test_main_page_validate_page_4_info(main_page: MainPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.set_text("4")
    page_info = main_page.get_all_data_for_a_column("Name")
    print(page_info)
    assert "Data can't be processed" not in page_info


def test_main_page_navigate_to_page_4_using_arrow_button(main_page: MainPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.set_text("3")
    main_page.click_on_right_arrow()
    page_info = main_page.get_all_data_for_a_column("Name")
    print(page_info)
    assert "Data can't be processed" not in page_info


def test_main_page_navigate_to_page_7_using_arrow_button(main_page: MainPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.set_text("6")
    main_page.click_on_right_arrow()
    page_info = main_page.get_all_data_for_a_column("ID")
    print(page_info)
    assert '70' in page_info


def test_main_page_navigate_to_page_10_using_arrow_button(main_page: MainPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.set_text("9")
    main_page.click_on_right_arrow()
    page_info = main_page.get_all_data_for_a_column("ID")
    print(page_info)
    assert '91' in page_info


def test_main_page_validate_page_10_info(main_page: MainPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.set_text("10")
    user_info = main_page.get_data_by_id("100", "Name")
    print(user_info)
    assert user_info != "null"


def test_main_page_enter_number_larger_than_number_of_pages_in_textbox_and_verify_app_not_navigated_to_page_1(main_page: MainPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.set_text("3")
    main_page.set_text("44")
    page_info = main_page.get_all_data_for_a_column("ID")
    print(page_info)
    assert '1' not in page_info
