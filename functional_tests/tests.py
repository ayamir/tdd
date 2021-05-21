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
        self.assertIn(row_text, [row.text for row in rows])

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
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')

        self.fail('Finish the test!')  # (5)
