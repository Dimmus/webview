import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class DefinitionExample(unittest.TestCase):
    '''
    This test...
      * Opens an existing Page called "Selenium Test Page"
      * adds a definition and example to the Page
      * takes a screenshot for verification

    '''


    def setUp(self):
        self.driver = webdriver.Firefox()
        #chrome driver option
        #self.driver = webdriver.Chrome('/home/ew2/PycharmProjects/chromedriver')
        propfile = open('properties.ini')
        items = [line.rstrip('\n') for line in propfile]
        self.authkey = items[0]
        self.pw = items[1]
        self.url = items[2]

    def tearDown(self):
        self.driver.save_screenshot('definition-example-test.png')
        self.driver.quit()

    def test_definition_example_editing(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(300)
        # login
        authKey = self.driver.find_element_by_name('auth_key')
        authKey.send_keys(self.authkey)
        pw = self.driver.find_element_by_name('password')
        pw.send_keys(self.pw)
        signin = self.driver.find_element_by_css_selector('button.standard')
        signin.click()
        self.driver.implicitly_wait(300)
        # open page
        pagelink = self.driver.find_element_by_link_text('Selenium Test Page')
        pagelink.click()
        self.driver.implicitly_wait(300)
        dest_element = self.driver.find_element_by_xpath('/html/body/section/div/div[2]/div[2]/div[1]/div[7]')
        # add definition
        source_element = self.driver.find_element_by_css_selector('dl.definition.ui-draggable')
        ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()
        dest_element.click()
        dest_element.click()
        # add example
        source_element = self.driver.find_element_by_css_selector('div.example.ui-draggable')
        ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()
        # clicking and waiting to force editor to refresh after drop
        self.driver.implicitly_wait(300)
        dest_element.click()
        dest_element.click()
        self.driver.implicitly_wait(300)
        dest_element.click()
        dest_element.click()
        self.driver.implicitly_wait(600)
        dest_element.click()
        dest_element.click()
        # savebutton = self.driver.find_element_by_xpath('(//button[@type="button"])[22]')
        # savebutton.click()


if __name__ == "__main__":
    unittest.main()

