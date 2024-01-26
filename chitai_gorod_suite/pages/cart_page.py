from selene import browser, have, be, command


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
        browser.execute_script("document.body.style.zoom='30%'")
        browser.element('.products__items').should(be.visible)
        browser.element('.delete-many').perform(command.js.click)
        return self

    def assert_cart_is_empty(self, text):
        browser.element('.cart-multiple-delete__title').should(
            have.text(text)
        )
        return self


cart = CartPage()

