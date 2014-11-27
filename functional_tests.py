import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.url = 'http://localhost:5000'

    def tearDown(self):
        self.browser.quit()

    def test_fresh_start_page(self):
        browser = self.browser

        browser.get(self.url)

        self.assertIn('Currency Converter', self.browser.title)

        # User inputs data into 'Amount' field
        amount_input = browser.find_element_by_name('amount')
        amount_input.send_keys('1')

        # user clicks Enter, the page updates and we should see result
        amount_input.send_keys(Keys.ENTER)

        browser.find_element_by_id("result")

    def test_form_errors(self):
        browser = self.browser

        browser.get(self.url)

        # User inputs nothing into required fields
        amount_input = browser.find_element_by_name('amount')
        amount_input.send_keys(Keys.ENTER)
        error = browser.find_element_by_class_name("amount-error")
        self.assertEqual(error.text, 'This field is required.')

        # User inputs invalid values
        amount_input = browser.find_element_by_name('amount')
        amount_input.send_keys('test')
        amount_input.send_keys(Keys.ENTER)
        error = browser.find_element_by_class_name("amount-error")
        msg = 'Not a valid float value Number must be between 0 and 10000.'
        self.assertEqual(error.text, msg)


if __name__ == '__main__':
    unittest.main()
