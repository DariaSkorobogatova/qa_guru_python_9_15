from selene import browser, be
import time


class ProductPage:
    def find_product(self, value):
        browser.element('.header-search__input').should(be.blank).type(
            value
        ).press_enter()
        return self

    def add_to_cart(self):
        browser.element('.products-list article:first-child').click()
        browser.element('.product-detail-offer .action-button').click()
        return self

    def enter_the_delivery_address(self, value):
        browser.element('#search-input').type(value).press_enter()
        time.sleep(2)
        browser.element('[data-qa=button-save-delivery-address]').click()
        return self

    def click_to_the_cart(self):
        browser.element('[data-qa=header-cart-button]').press_enter()
        return self

