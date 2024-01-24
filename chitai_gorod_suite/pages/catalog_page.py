from selene import browser, have


class CatalogPage:
    def choose_category(self, value):
        browser.all('.categories-menu__item-title').element_by(
            have.exact_text(value)
        ).click()

    def assert_right_category(self, text):
        browser.element('.app-catalog-page__title').should(
            have.text(text)
        )
        return self


catalog = CatalogPage()
