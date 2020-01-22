from selenium.webdriver.common.by import By
from Data.test_data import ProfilePageEventsMenu
from Data.test_data import ProfileMenuPageHeaderInfo


class LoginPageLocators:
    """
    Locators for login page.
    """
    # button for opening form of authorization
    SIGNIN = (By.CLASS_NAME, 'MuiButton-label')

    # form of signin/upR

    EMAIL_SIGNIN = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    BUTTON_SIGIN = (
        By.CSS_SELECTOR,
        ".auth .MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-fullWidth:nth-child(2)")
    CLEAR = (
        By.CSS_SELECTOR,
        ".auth .MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-fullWidth:nth-child(1)")


class RegisterLocators:
    """
    Locators for registration form.
    """
    REGISTER = (
        By.CSS_SELECTOR,
        ".MuiTabs-scroller.MuiTabs-fixed button:nth-child(2)")
    EMAIL_SIGNIN = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    RE_PASSWORD = (By.NAME, "RepeatPassword")
    CLEAR = (
        By.CSS_SELECTOR,
        ".MuiDialogActions-root.MuiDialogActions-spacing button:nth-child(1)")
    SIGNUP = (By.CSS_SELECTOR,)


class NavigationMenuLocators:
    """
    Locators for right Navigation menu.
    """
    Home = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(1)")
    PROFILE = (
        By.CSS_SELECTOR,
        "nav ul.list-unstyled .sidebar-header:nth-child(2)")
    SEARCH_USER = (
        By.CSS_SELECTOR,
        "nav ul.list-unstyled .sidebar-header:nth-child(3)")
    COMUNA = (
        By.CSS_SELECTOR,
        "nav ul.list-unstyled .sidebar-header:nth-child(4)")
    # selector if actor is USER
    CONTACT_US = (
        By.CSS_SELECTOR,
        "nav ul.list-unstyled .sidebar-header:nth-child(5)")
    CATEGORIES = (
        By.CSS_SELECTOR,
        "nav ul.list-unstyled .sidebar-header:nth-child(5)")
    USERS = (
        By.CSS_SELECTOR,
        "nav ul.list-unstyled .sidebar-header:nth-child(6)")
    EVENTS = (
        By.CSS_SELECTOR,
        "nav ul.list-unstyled .sidebar-header:nth-child(7)")


# search available on every page of EventExpress
class SearchEventPanelLocators():
    """
    Locators for searching and filter functionality.
    """
    SEARCH_FIELD = (
        By.CSS_SELECTOR, ".MuiInputBase-input")
    SELECT_DATE_FIELD = (
        By.CSS_SELECTOR, ".react-datepicker-ignore-onclickoutside")
    DATE_FROM = (
        By.CSS_SELECTOR, "div.form-group:nth-child(2) > div:nth-child(2)")
    DATE_TO = (By.CSS_SELECTOR, "div.form-group:nth-child(3) > div:nth-child(2) > div:nth-child(1)")
    RADIO_BUTTON_BLOCKED = (By.CSS_SELECTOR, "label.MuiFormControlLabel-root:nth-child(1)")
    RADIO_BUTTON_UNBLOCKED = (By.CSS_SELECTOR, "label.MuiFormControlLabel-root:nth-child(2)")
    RADIO_BUTTON_ALL = (By.CSS_SELECTOR, "label.MuiFormControlLabel-root:nth-child(3)")
    HASHTAGS_FIELD = (By.CSS_SELECTOR, ".rw-widget-input")
    HASHTAGS_SELECT = (By.ID, "rw_1_listbox > li")  # nth-child(NAMBER_FIELD)
    BUTTON_MORE_FILTER = (
        By.CSS_SELECTOR,
        ".box > div:nth-child(2) > button:nth-child(1)")
    BUTTON_LESS = (
        By.CSS_SELECTOR,
        ".box > div:nth-child(6) > button:nth-child(1)")
    BUTTON_SEARCH = (
        By.CSS_SELECTOR,
        "button.MuiButtonBase-root:nth-child(2) > span:nth-child(1)")
    BUTTON_RESET = (
        By.CSS_SELECTOR,
        "button.MuiButton-textPrimary:nth-child(1) > span:nth-child(1)")
    #NAV_PANEL = (By.CSS_SELECTOR, ".flex-column > div:nth-child(4)")
    FIELD_NAME_EVENT = (
        By.CSS_SELECTOR,
        "div.col-12:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)")


class SearchEventData():
    """
    Locators for search element functionality.
    """
    NAV_PANEL = (By.CSS_SELECTOR, ".flex-column > div:nth-child(4)")
    NAME_EVENT = (
        By.CSS_SELECTOR,
        "div.col-12:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)")


# page for communication users with admins
class ContactUsPageLocators():
    """
    Locators for Contact Us Page.
    """
    DESCRIPTION = (By.CSS_SELECTOR, 'textarea')
    SUBMIT = (By.CSS_SELECTOR, 'button:nth-child(3)')
    MES = (
        By.CSS_SELECTOR,
        '#root > div.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomLeft > div')
    CLEAR = (By.CSS_SELECTOR, 'button:nth-child(4) > span.MuiButton-label')
    REQUIRED = (By.CSS_SELECTOR, 'p')
    TYPE = (By.TAG_NAME, "select")
    LIST = (By.CSS_SELECTOR, ".form-control")


# user communication page
class ComunaPageLocators():
    """
    Locators for Comuna Page.
    """
    SELECT_CORRESPONDENCE = (By.CSS_SELECTOR, 'button > div')
    SEND_MESSAGE_FIELD = (
        By.CSS_SELECTOR,
        '.card-footer > form > div > div > input')
    SEND_BUTTON = (By.CSS_SELECTOR, '.MuiButton-label')
    OUR_MESSAGE = (By.CSS_SELECTOR, '.msg_card_body > div:nth-child(4) > div')
    MESSAGE = (By.CSS_SELECTOR, '.msg_card_body > div:nth-child(3) > div')


# profile with information about events adn on the up of page is personal info
class ProfileMenuLocators:
    """
    Profile page and menu locators.
    """
    # ToDo the same as for NavigationMenuLocators class
    ADD_EVENT = (
        By.CSS_SELECTOR,
        ".MuiTabs-scroller.MuiTabs-fixed [type='button']:nth-child(5)")


class ProfilePageEventsMenuLocators:
    """
    Events menu object locators.
    """
    # User
    locators_dict = {ProfilePageEventsMenu.FUTURE_EVENTS: (By.CSS_SELECTOR, '#full-width-tab-0'),
                     ProfilePageEventsMenu.ARCHIVE_EVENTS: (By.CSS_SELECTOR, '#full-width-tab-1'),
                     ProfilePageEventsMenu.VISITED_EVENTS: (By.CSS_SELECTOR, '#full-width-tab-2'),
                     ProfilePageEventsMenu.EVENTS_TO_GO: (By.CSS_SELECTOR, '#full-width-tab-3'),
                     ProfilePageEventsMenu.ADD_EVENT: (By.CSS_SELECTOR, '#full-width-tab-4'),
                     # Whole panel
                     'EVENT_MENU_PANEL': (By.CSS_SELECTOR, '.mt-2 > header div'),
                     'COUNT_MENU_ITEMS': (By.CSS_SELECTOR, 'button[id*="full"]'),
                     'ACTIVE_TAB_MARKER': (By.CSS_SELECTOR, 'button[aria-selected="true"]'),
                     'TABS_COUNT': (By.CSS_SELECTOR, 'button[id*="full"]'),
                     }

    TAB_INDICATOR_DICT = {
                     'FUTURE EVENTS': (By.CSS_SELECTOR, 'div[id="scrollable-force-tabpanel-0"'),
                     'ARCHIVE EVENTS': (By.CSS_SELECTOR, "div[id='scrollable-force-tabpanel-1']"),
                     'VISITED EVENTS': (By.CSS_SELECTOR, "div[id='scrollable-force-tabpanel-2']"),
                     'EVENTS TO GO': (By.CSS_SELECTOR, "div[id='scrollable-force-tabpanel-3']"),
                     'ADD EVENT': (By.CSS_SELECTOR, "div[id='scrollable-force-tabpanel-4']"),
                     'ACTIVE TAB': (By.CSS_SELECTOR, 'button[aria-selected="true"]'),
                     }

    TABS = (By.XPATH, '//button[@role="tab"]')


class ProfileMenuPageHeaderInfoLocators:
    """
    Locators for user info page header (central header).
    """
    # User  .row:nth-child(1) > .col-4
    locators_dict = {  # ProfileMenuPageHeaderInfo.USER_NAME_LABEL: (By.CSS_SELECTOR, '.row:nth-child(1) > .col-4'),
        # ProfileMenuPageHeaderInfo.USER_NAME_DATA: (By.CSS_SELECTOR, '.row:nth-child(1) > .col-8'),
        # ProfileMenuPageHeaderInfo.USER_AGE_LABEL: (By.CSS_SELECTOR, '.row:nth-child(2) > .col-4'),
        # ProfileMenuPageHeaderInfo.USER_AGE_DATA: (By.CSS_SELECTOR, '.row:nth-child(2) > .col-8'),
        # ProfileMenuPageHeaderInfo.USER_GENDER_LABEL: (By.CSS_SELECTOR, '.row:nth-child(3) > .col-4'),
        # ProfileMenuPageHeaderInfo.USER_GENDER_DATA: (By.CSS_SELECTOR, '.row:nth-child(3) > .col-8'),
        # ProfileMenuPageHeaderInfo.USER_EMAIL_LABEL: (By.CSS_SELECTOR, '.row:nth-child(4) > .col-4'),
        # ProfileMenuPageHeaderInfo.USER_EMAIL_DATA: (By.CSS_SELECTOR, '.row:nth-child(4) > .col-8'),
        # ProfileMenuPageHeaderInfo.USER_INTERESTS_LABEL: (By.CSS_SELECTOR, '.row:nth-child(5) > .col-4'),
        'USER_INTERESTS_DATA': (By.CSS_SELECTOR, '.row:nth-child(5) > .col-4')
    }


class HomePageOptionsPanelLocators:
    """
    Left top menu (config, notification, logout) with user logo.
    """
    # button[type = "button"][title = "Sign out"]
    # user_info_css = 'h4.gs_copied'
    locators_dict = {
        'logout_button': (By.CSS_SELECTOR, 'button[title ="Sign out"]'),
        'user_info': (By.CSS_SELECTOR, 'h4.gs_copied'),
    }


class CartPanelsAtProfilePageLocators:
    """
    Locators for Event menu object.
    """
    # child(cart_index). cart_index = 0 - EMPTY; >0 carts
    # User
    locators_dict = {
        'CART_NTH': (
            By.CSS_SELECTOR,
            '.mt-2 .col-12:nth-child(3)'),
        'BLANK_CART': (
            By.CSS_SELECTOR,
            '.w-100 .h1'),
        'CART_PANEL': (
            By.CSS_SELECTOR,
            '#main>.mt-2 .row:nth-child(1)'),
        'ADD_EVENT_CART_CLEAR_BUTTON': (
            By.CSS_SELECTOR,
            'form button')}


class CreateEvent:
    UPLOAD_PICTURE = (By.CSS_SELECTOR, ".placeholder-preview > input ")
    EVENT_TITLE = (By.NAME, "title")
    CALENDAR = (By.CSS_SELECTOR, ".react-datepicker-wrapper")
    CALENDAR_VALUE = (
        By.CSS_SELECTOR,
        ".react-datepicker-ignore-onclickoutside")
    # calendar begin date of event
    FROM_DATE = (By.CSS_SELECTOR, ".react-datepicker-popper")
    # description about future event
    DESC_TEXT = (By.CSS_SELECTOR, "[name='description']")
    CATEGORY = (By.CSS_SELECTOR, ".rw-input-reset")
    LST_CATEGORIES = (By.CSS_SELECTOR, ".rw-popup-container ul > li")
    # country and city
    COUNTRY_FIELD = (By.ID, 'age-native-simple')
    COUNTRY = (By.NAME, "countryId")
    CITY = (By.NAME, "cityId")
    SAVE = (By.CSS_SELECTOR, "[type='Submit']")
    SUCCESS_MSG = (By.ID, "client-snackbar")


class CategoriesLocators:
    """
    Locators for Categories Page.
    """
    ADD_CATEGORY_BUTTON = (By.CSS_SELECTOR, '.fa-plus-circle')
    #ADD_CATEGORY_BUTTON = (By.CSS_SELECTOR, '.f-plus-circle')
    ADD_CATEGORY_FIELD = (By.NAME, 'category')
    CATEGORIES = (By.TAG_NAME, 'tr')
    CAT = (By.XPATH, '//tr[3]/td[1]')
    ADD_CATEGORY_CROSS = (By.CSS_SELECTOR, '.fa-times > path')
    ADD_CATEGORY_CHECK = (By.CSS_SELECTOR, '.fa-check')


class EditYourProfile:
    """
    Locators for Edit Profile Page.
    """
    EDIT_PROFILE = (By.CSS_SELECTOR, ':nth-child(1) > button')
    CHANGE_AVATAR = (
        By.XPATH,
        '/html/body/div[1]/div[3]/div/div[1]/div[1]/div[1]/p')
    CHANGE_USERNAME = (
        By.XPATH,
        '/html/body/div[1]/div[3]/div/div[2]/div[1]/div[1]/p[1]')
    CHANGE_GENDER = (
        By.XPATH,
        '/html/body/div[1]/div[3]/div/div[3]/div[1]/div[1]/p[1]')
    CHANGE_DATE_OF_BIRTH = (By.XPATH, '//*[@id="panel3bh-header"]/div[1]/p[1]')
    CHANGE_FAVORITE_CATEGORIES = (
        By.XPATH, '//*[@id="panel4bh-header"]/div[1]/p[1]')
    CHANGE_PASSWORD = (
        By.XPATH,
        '/html/body/div[1]/div[3]/div/div[6]/div[1]/div[1]/p')
