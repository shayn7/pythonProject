from playwright.sync_api import expect
from pages.page_objects.add_new_member_page import AddNewMemberPage
from pages.page_objects.main_page import MainPage
import random


def test_add_new_member_page_user_gets_unused_id(main_page: MainPage, add_new_member_page: AddNewMemberPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.click_on_add_person()
    expect(add_new_member_page.add_new_member_window).to_be_visible()
    add_new_member_page.add_new_user("george", "costenza")
    main_page.set_text("11")
    page_info = main_page.get_all_data_for_a_column("ID")
    print(page_info)
    assert '1' not in page_info


def test_add_new_member_page_add_user_with_number_in_name_field(main_page: MainPage,
                                                                add_new_member_page: AddNewMemberPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.click_on_add_person()
    expect(add_new_member_page.add_new_member_window).to_be_visible()
    add_new_member_page.add_new_user("33", "costenza")
    main_page.set_text("11")
    name_data = main_page.get_all_data_for_a_column("Name")
    family_data = main_page.get_all_data_for_a_column("Family")
    print(name_data)
    print(family_data)
    assert "33" not in name_data
    assert "33" not in family_data


def test_add_new_member_page_verify_user_entered_with_correct_info(main_page: MainPage,
                                                                   add_new_member_page: AddNewMemberPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.click_on_add_person()
    expect(add_new_member_page.add_new_member_window).to_be_visible()
    num = random.randint(0, 1000)
    add_new_member_page.add_new_user("george" + str(num), "costenza" + str(num))
    main_page.set_text("11")
    name_data = main_page.get_all_data_for_a_column("Name")
    family_data = main_page.get_all_data_for_a_column("Family")
    print(name_data)
    print(family_data)
    assert "george" + str(num) in name_data
    assert "costenza" + str(num) in family_data


def test_add_new_member_page_add_user_with_large_amount_of_characters(main_page: MainPage,
                                                                      add_new_member_page: AddNewMemberPage) -> None:
    main_page.go_to_page()
    expect(main_page.table_header).to_be_visible()
    main_page.click_on_add_person()
    expect(add_new_member_page.add_new_member_window).to_be_visible()
    add_new_member_page.add_new_user("gegeorgegeorgegeorgegeorgeorgegeorgegeorgegeorgegeorgegeorgegeorgegeorge",
                                     "costenzacostenzacostenzacostenzacostenzacostenzacostenzacostenzacostenzacostenza")
    main_page.set_text("11")
    name_data = main_page.get_all_data_for_a_column("Name")
    family_data = main_page.get_all_data_for_a_column("Family")
    print(name_data)
    print(family_data)
    assert 'costenzacostenzacostenzacostenzacostenzacostenzacostenzacostenzacostenzacostenza' not in name_data
    assert 'costenzacostenzacostenzacostenzacostenzacostenzacostenzacostenzacostenzacostenza' not in family_data
