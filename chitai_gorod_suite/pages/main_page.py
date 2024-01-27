from selene import browser, have, be


class MainSitePage:
    def open(self):
        browser.open('/')
        browser.element('[class="button change-city__button change-city__button--accept blue"]').click()
        return self

    def close_change_city_popup(self):
        if browser.element('.change-city').wait_until(be.visible):
            browser.element('.change-city__button--accept').click()

    def change_city(self):
        self.close_change_city_popup()
        browser.element('.header-city__title').click()
        browser.element('.change-city__button--cancel').click()
        return self

    def choose_city(self, value):
        browser.all('.city-modal__popular-item').element_by(
            have.exact_text(value)
        ).click()

    def assert_city_changed(self, text):
        browser.element('.change-city__title').should(
            have.text(text)
        )
        return self

    def click_catalog(self):
        self.close_change_city_popup()
        browser.element('.catalog__button').should(be.visible).click()
        return self


main_page = MainSitePage()




