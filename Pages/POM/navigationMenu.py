from Locators.locators import NavigationMenuLocators



class NavigationMenu():

    def __init__(self, browser):
        self.browser = browser
        self.locator = NavigationMenuLocators


    def click_on_home(self):
        self.browser.click_on_element(self.locator.Home)

    def click_on_profile(self):
        self.browser.click_on_element(self.locator.PROFILE)

    def click_on_search_user(self):
        self.browser.click_on_element(self.locator.SEARCH_USER)

    def click_on_comuna(self):
        self.browser.click_on_element(self.locator.COMUNA)