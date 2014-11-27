import unittest

from selenium import webdriver


class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_fresh_start_page(self):
        self.browser.get('http://localhost:5000')

        self.assertIn('Currency Converter', self.browser.title)
        self.fail('Finish the test!')
        # User inputs data into 'Amount' field

        # user select value from 'From currency' field

        # user select value from 'To currency' field

        # users clicks on 'Convert' button

        # users sees in '#result' result

if __name__ == '__main__':
    unittest.main()
