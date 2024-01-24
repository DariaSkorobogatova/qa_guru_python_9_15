import allure
from chitai_gorod_suite.pages.main_page import main_page
from chitai_gorod_suite.pages.catalog_page import catalog


@allure.title('Check going to chosen category')
def test_hobby_category():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Click catalog'):
        main_page.click_catalog()

    with allure.step('Choose category'):
        catalog.choose_category('Творчество и хобби')
        catalog.choose_category('Мыловарение, свечи')

    with allure.step('Assert went to right category'):
        catalog.assert_right_category('МЫЛОВАРЕНИЕ, СВЕЧИ')
