import unittest
from selenium import webdriver
from time import sleep
from pageObj.searchPage import SearchPage
from pageObj.listPage import ListPage


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('tests\\chromedriver.exe')
        self.driver.maximize_window()

        self.searchMain = SearchPage(self.driver)
        self.listMain = ListPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_one_empty_search(self):
        self.driver.get('http://localhost:3000/shows')
        msg = self.searchMain.get_empty_search_message()
        self.assertEqual(msg, 'Search cannot be empty.')
        sleep(5)
        print('Empty query validated')
        

    def test_two_batman_flow(self):
        self.driver.get('http://localhost:3000/shows')
        self.searchMain.set_search_txt('batman')
        self.searchMain.click_search_btn()
        self.driver.back()
        self.searchMain.click_search_btn()
        self.listMain.changeResultBackgroundBackground("Batman Unlimited")
        self.listMain.click_back_btn()
        txt = self.searchMain.get_input_text()
        self.assertEqual(txt, "")
        sleep(3)
        print('Flow complete')
        
        
if __name__ == '__main__':
    unittest.main()