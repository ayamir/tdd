from django.test import LiveServerTestCase
from msedge.selenium_tools import EdgeOptions, Edge
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(LiveServerTestCase):  # (1)
    def setUp(self):  # (2)
        options = EdgeOptions()
        options.use_chromium = True
        options.binary_location = r'/usr/bin/microsoft-edge-dev'
        options.set_capability("platform", "LINUX")  # (2)

        webdriver_path = r'/home/ayamir/.local/bin/msedgedriver'
        self.browser = Edge(options=options, executable_path=webdriver_path)

    def tearDown(self):  # (3)
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row_text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)  # (3)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


        self.fail('Finish the test!')  # (5)


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
