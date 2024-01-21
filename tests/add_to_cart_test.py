import allure
from chitai_gorod_suite.pages.main_page import MainPage
from chitai_gorod_suite.pages.product_page import ProductPage
from chitai_gorod_suite.pages.cart_page import CartPage


@allure.title('Add item to cart')
def test_add_product():
    main_page = MainPage()
    product = ProductPage()
    cart = CartPage()

    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Enter the item name'):
        product.find_product('Понедельник начинается в субботу')

    with allure.step('Add to cart'):
        product.add_to_cart()

    with allure.step('Go to cart'):
        cart.go_to_cart()

    with allure.step('Assert'):
        cart.assert_item_in_cart('Понедельник начинается в субботу')

