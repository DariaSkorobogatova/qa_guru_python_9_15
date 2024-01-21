import allure
from chitai_gorod_suite.pages.main_page import MainPage
from chitai_gorod_suite.pages.catalog_page import CatalogPage


@allure.title('Check going to chosen category')
def test_hobby_category():
    main_page = MainPage()
    catalog_page = CatalogPage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Click catalog'):
        main_page.click_catalog()

    with allure.step('Choose category'):
        catalog_page.choose_category('Творчество и хобби')
        catalog_page.choose_category('Мыловарение, свечи')

    with allure.step('Assert went to right category'):
        catalog_page.assert_right_category('МЫЛОВАРЕНИЕ, СВЕЧИ')
