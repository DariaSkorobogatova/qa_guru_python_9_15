import allure
from chitai_gorod_suite.pages.main_page import main_page
from chitai_gorod_suite.pages.product_page import product
from chitai_gorod_suite.pages.cart_page import cart


@allure.title('Clear the cart test')
def test_clear_cart():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Add item to cart'):
        product.find_product('голодные игры и вспыхнет пламя')
        product.add_to_cart()

    with allure.step('Go to cart'):
        cart.go_to_cart()
        main_page.close_change_city_popup()

    with allure.step('Clear the cart'):
        cart.clear_cart()

    with allure.step('Assert cart is empty'):
        cart.assert_cart_is_empty('Корзина очищена')
    # почему когда запушил закоментированный шаг, он все равно отображается в отчете?
    # именно этот шаг тебе фейлит отчет, а не очистка корзины - она по отчету работает
    # проверь репу - увидишь, о чем я говорю
    # есть вероятность, что Jenkins не подтягивает новые изменения?



