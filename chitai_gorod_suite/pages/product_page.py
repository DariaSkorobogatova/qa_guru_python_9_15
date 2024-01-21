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



