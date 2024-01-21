from selene import browser, have


class CertificatePage:
    def click_present_certificates(self):
        browser.element('a[href="/certificate"]').click()
        return self

    def certificate_block_titles(self):
        return browser.element('.certificate-page__block-wrapper').all(
            '.certificate-block__title'
        )

    def should_have_titles(self, title1, title2):
        self.certificate_block_titles().should(have.texts(title1, title2))
