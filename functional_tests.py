from msedge.selenium_tools import EdgeOptions, Edge
import unittest


class NewVisitorTest(unittest.TestCase):  # (1)
    def setUp(self):  # (2)
        options = EdgeOptions()
        options.use_chromium = True
        options.binary_location = r'/usr/bin/microsoft-edge-dev'
        options.set_capability("platform", "LINUX")  # (2)

        webdriver_path = r'/home/ayamir/.local/bin/msedgewebdriver'
        self.browser = Edge(options=options, executable_path=webdriver_path)

    def tearDown(self):  # (3)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')  # (3)
        self.assertIn('To-Do', self.browser.title)  # (4)
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
