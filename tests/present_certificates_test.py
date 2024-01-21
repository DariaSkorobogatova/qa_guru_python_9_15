import allure
from chitai_gorod_suite.pages.main_page import MainPage
from chitai_gorod_suite.pages.certificates_page import CertificatePage


@allure.title('Clear the cart test')
def test_type_certificates():
    main_page = MainPage()
    certificates_page = CertificatePage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Go to present certificate tab'):
        certificates_page.click_present_certificates()

    with allure.step('Assert certificates blocks are there'):
        certificates_page.should_have_titles('Электронный сертификат', 'Пластиковый сертификат')



