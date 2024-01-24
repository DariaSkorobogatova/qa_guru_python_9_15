import allure
from chitai_gorod_suite.pages.main_page import main_page


@allure.title('Change city test')
def test_change_city():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Click change city'):
        main_page.change_city()

    with allure.step('Choose city'):
        main_page.choose_city('Казань')

    with allure.step('Assert city has been changed'):
        main_page.change_city()
        main_page.assert_city_changed('Ваш город — Казань?')



