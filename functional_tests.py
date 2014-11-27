import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_fresh_start_page(self):
        browser = self.browser

        browser.get('http://localhost:5000')

        self.assertIn('Currency Converter', self.browser.title)

        # User inputs data into 'Amount' field
        amount_input = browser.find_element_by_name('amount')
        amount_input.send_keys('1')
        # user clicks Enter, the page updates and we should see result
        amount_input.send_keys(Keys.ENTER)

        result_text = browser.find_element_by_id("result")
        self.fail('Finish the test!')

        # user select value from 'From currency' field

        # user select value from 'To currency' field

        # users clicks on 'Convert' button

        # users sees in '#result' result

if __name__ == '__main__':
    unittest.main()
