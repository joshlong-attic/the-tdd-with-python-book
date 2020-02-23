from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        # Edit has heard about a cool new online to do app. She goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


# she is invited to enter a todo item straight away
# she types 'buy peacock feathers' into a text box (edit's hobby is tying fly-fishing lures)
# when she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list
# there is still a text box inviting her to add another item.
# She enters "use peacock feathers to make a fly" (Edith is very methodical)
# the page updates again, and now show sboth items on her list

# Edith wonders whether the site will remember her list.
# Then she sees that the site has generated a unique URL for her -- there is some explanatory text to that effect.
# She visits the URL - her todo list is still there.
# Satisfid, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
