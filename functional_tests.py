from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Kathleen thinks of something she or Ryan needs to do.
        # She goes to the homepage of a new onine Todo app
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        
        # She types "Buy peackock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
        # When selfhe hits enter, the page updates, and now lists
        # 1: Buy peacock feathers
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        # There is still a text box inviting her to add another item.
        # She enters "Make flyfishing fly using peacock feathers" and presses enter
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # The page updates again, now showing both items
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        
        # Edith wonders if the site will remember her list, but then
        # she sees that the site made her a unique url for her list. 
        # There is some text explaining the situation.
        self.fail('Finish the test')
        # She visits that URL and her to-do list is still there
        
        # Satisfied, she goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
