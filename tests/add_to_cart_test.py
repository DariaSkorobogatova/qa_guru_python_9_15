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


#
#     with allure.step('Enter the delivery address'):
#         product.enter_the_delivery_address('Санкт-Петербург, Лиговский проспект, 50')
#
#     with allure.step('Click to the cart icon'):
#         product.click_to_the_cart()
#
#     with allure.step('Checkout'):
#         product.click_to_the_checkout_button()
#
#     with allure.step('Assert'):
#         product.assert_checkout()
#
#
# @allure.title('Add product to cart with pickup')
# def test_add_product_to_cart_with_pickup():
#     product = Product()
#
#     with allure.step('Open main page'):
#         product.open_main_page()
#
#     with allure.step('Enter the product name'):
#         product.search_product('METRO Chef Лапша гречневая, 600г')
#
#     with allure.step('Add to cart'):
#         product.add_to_cart()
#
#     with allure.step('Change delivery to pickup'):
#         product.click_to_the_pickup_button()
