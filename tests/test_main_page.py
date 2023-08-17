from playwright.sync_api import expect

from pages.page_objects.main_page import MainPage


# def test_main_page_validate_relevant_users_on_selected_page(main_page: MainPage) -> None:
#     main_page.go_to_page()
#     expect(main_page.table_header).to_be_visible()
#     main_page.set_text("3")
#     expected_users = """
# 21      Joseph  Daniel
# 22      Lucas   Oliver
# 23      Jessica Henry
# 24      Amelia  Evelyn
# 25      Henry   Ethan
# 26      Abigail Ethan
# 27      Andrew  Sophia
# 28      Andrew  Joshua
# 29      Jacob   Mia
# 30      Emma    Henry
# """
#     actual_users = main_page.get_users_on_page()
#     print(expected_users)
#     print(actual_users)
#     assert main_page.strip_white_space(actual_users) == main_page.strip_white_space(expected_users)
#
#
# def test_main_page_validate_relevant_users_of_selected_page_after_refresh(main_page: MainPage) -> None:
#     main_page.go_to_page()
#     expect(main_page.table_header).to_be_visible()
#     main_page.set_text("3")
#     expected_users = """
#     21      Joseph  Daniel
#     22      Lucas   Oliver
#     23      Jessica Henry
#     24      Amelia  Evelyn
#     25      Henry   Ethan
#     26      Abigail Ethan
#     27      Andrew  Sophia
#     28      Andrew  Joshua
#     29      Jacob   Mia
#     30      Emma    Henry
#     """
#     actual_users = main_page.get_users_on_page()
#     assert main_page.strip_white_space(actual_users) == main_page.strip_white_space(expected_users)
#     main_page.reload_page()
#     actual_users_after_reloading_the_page = main_page.get_users_on_page()
#     assert main_page.strip_white_space(actual_users_after_reloading_the_page) != main_page.strip_white_space(
#         expected_users)


def test_main_page_vali(main_page: MainPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.click_on_add_person()
