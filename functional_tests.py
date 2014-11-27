from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:5000')

elem = browser.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")

assert 'Hello World!' in source_code
