from selene import browser, have


class MainPage:
    def open(self):
        browser.open('/')
        return self

    def change_city(self):
        browser.element('.header-city__title').click()
        browser.element('.change-city__button--cancel').click()
        return self

    def choose_city(self, value):
        browser.all('.city-modal__popular-item').element_by(
            have.exact_text(value)
        ).click()

    def assert_city_changed(self, text):
        browser.element('.header-city__title').should(
            have.text(text)
        )
        return self

    def click_catalog(self):
        browser.element('.catalog__button-image').click()
        return self



