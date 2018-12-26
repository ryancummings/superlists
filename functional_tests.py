from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Kathleen thinks of something she or Ryan needs to do.
        # She goes to the homepage of a new onine Todo app
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        # She is invited to enter a to-do item straight away
        
        # She types "Buy peackock feathers" into a text box
        
        # When selfhe hits enter, the page updates, and now lists
        # 1: Buy peacock feathers

        # There is still a text box inviting her to add another item.

        # She enters "Make flyfishing fly using peacock feathers" and presses enter

        # The page updates again, now showing both items

        # Edith wonders if the site will remember her list, but then
        # she sees that the site made her a unique url for her list. 
        # There is some text explaining the situation.

        # She visits that URL and her to-do list is still there
        
        # Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
