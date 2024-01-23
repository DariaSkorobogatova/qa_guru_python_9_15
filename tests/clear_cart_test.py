import allure
from chitai_gorod_suite.pages.main_page import MainPage
from chitai_gorod_suite.pages.product_page import ProductPage
from chitai_gorod_suite.pages.cart_page import CartPage


@allure.title('Clear the cart test')
def test_clear_cart():
    main_page = MainPage()
    product = ProductPage()
    cart = CartPage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Add item to cart'):
        product.find_product('голодные игры и вспыхнет пламя')
        product.add_to_cart()

    with allure.step('Go to cart'):
        cart.go_to_cart()

    with allure.step('Clear the cart'):
        cart.clear_cart()

    with allure.step('Assert cart is empty'):
        cart.assert_cart_is_empty('Корзина очищена')



