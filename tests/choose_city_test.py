import allure
from chitai_gorod_suite.pages.main_page import MainPage


@allure.title('Change city test')
def test_clear_cart():
    main_page = MainPage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Click change city'):
        main_page.change_city()

    with allure.step('Choose city'):
        main_page.choose_city('Казань')

    with allure.step('Assert city has been changed'):
        main_page.assert_city_changed('Казань')



