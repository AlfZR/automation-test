class SearchPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_bar = "//*[@name='search']"

        self.search_btn = "//*[@type='submit']"

        self.empty_search_msg = "//*[@data-error='wrong']"


    def set_search_txt(self, text):
        """
        Enter something in the search input
        """
        txt_input = self.driver.find_element_by_xpath(self.search_bar)
        txt_input.clear()
        txt_input.send_keys(text)
        print("Text set")

    def click_search_btn(self):
        """
        Click on the search button
        """
        btn = self.driver.find_element_by_xpath(self.search_btn)
        btn.click()
        print("Clicked on search button")

    def get_empty_search_message(self):
        """
        Get the error message when searching with an empty query
        """
        self.click_search_btn()
        errorMsg = self.driver.find_element_by_xpath(self.empty_search_msg)
        return errorMsg.text

    def get_input_text(self):
        """
        Get the text in the search input
        """
        txt_input = self.driver.find_element_by_xpath(self.search_bar)
        return txt_input.text