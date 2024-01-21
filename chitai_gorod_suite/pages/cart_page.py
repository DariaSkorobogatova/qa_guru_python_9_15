from selene import browser, have
import time


class CartPage:
    def go_to_cart(self):
        browser.element('.header-cart').click()
        return self

    def assert_item_in_cart(self, text):
        browser.element('.product-title__head').should(
            have.text(text)
        )
        return self

    def clear_cart(self):
        browser.element('.header-cart').click()
        time.sleep(3)
        browser.element('.delete-many').click()
        return self

    def assert_cart_is_empty(self, text):
        browser.element('.cart-multiple-delete__title').should(
            have.text(text)
        )
        return self

