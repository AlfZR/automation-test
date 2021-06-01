from time import sleep

class ListPage():

    def __init__(self, driver):
        self.driver = driver

        self.second_item = "(//div[@class='card-action light-blue darken-4']//a[contains(text(),'URL')])[2]"

        self.back_btn = "//a[contains(text(), 'Back')]"

        self.cardFromTitle = "(.//span[text()='Batman Unlimited']/.//ancestor::div[contains(@class,'card')])[1]"

        self.testColor = "#4a148c"


    def click_second_item(self):
        """
        Click on the second item URL
        """
        second_itm = self.driver.find_element_by_xpath(self.second_item)
        second_itm.click()
        print('Clicked on second item')

    def click_back_btn(self):
        """
        Click on the back button
        """
        back_btn = self.driver.find_element_by_xpath(self.back_btn)
        back_btn.click()
        print('Clicked on back button')

    def changeResultBackgroundBackground(self, title):
        """
        Change the background color of a given card
        """
        card = self.driver.find_element_by_xpath(self.cardFromTitle.format(title))
        self.driver.execute_script("arguments[0].setAttribute('style', 'background-color: "+self.testColor+" !important')", card)
        self.driver.execute_script("arguments[0].scrollIntoView();", card)
        sleep(3)
        print('Background color changed')
