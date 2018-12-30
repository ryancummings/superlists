from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidently tries to submit an empty list item.
        # She hist Enter on the empty input box

        # The page refreshes and there is an error message
        # that list items cannot be blank.

        # She tries again with some text, which works
        
        # She tries to submit a second blank list item
        # and receies a similar warning.

        # And she can correct it by filling in some text
        self.fail('write me!')
