from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import unittest
import time

MAX_WAIT = 5

class NewVisitorTest(LiveServerTestCase):  # (1)
    def setUp(self):  # (2)
        self.browser = webdriver.Chrome()

    def tearDown(self):  # (3)
        self.browser.quit()

    # def test_can_start_a_list_and_retrieve_it_later(self):
    #     self.browser.get(self.live_server_url)  # (3)
    #
    #     # she is invited to enter a to-do item straight away
    #     inputbox = self.browser.find_element_by_id('id_new_item')
    #     inputbox.send_keys('Buy peacock feathers')
    #     inputbox.send_keys(Keys.ENTER)
    #     self.wait_for_row_in_list_table('1: Buy peacock feathers')
    #
    #     inputbox = self.browser.find_element_by_id('id_new_item')
    #     inputbox.send_keys('Use peacock feathers to make a fly')
    #     inputbox.send_keys(Keys.ENTER)
    #
    #     self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
    #
    #     self.fail('Finish the test!')  # (5)

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.browser.quit()

        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)


if __name__ == '__main__':  # (6)
    unittest.main(warnings='ignore')  # (7)

# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage.

# She is invited to enter a to-do item straight away

# She types "Buy peacock features" into a text box (Edith's hobby
# is tying fly-fishing lures)

# when she hits enter, the page updates, and now the page list
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both item on her list

# Edith wonder whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.
# Satisfied, she goes back to sleep
