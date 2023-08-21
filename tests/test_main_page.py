from playwright.sync_api import expect

from pages.page_objects.main_page import MainPage


def test_main_page_validate_page_4_info(main_page: MainPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.set_text("4")
    page_info = main_page.get_all_data_for_a_column("Name")
    print(page_info)
    assert "Data can't be processed" not in page_info
