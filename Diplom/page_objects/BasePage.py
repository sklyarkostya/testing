import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver


class BasePage:
    """
    Basic methods that can be used on any page.
    """

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15

    def __element(self, selector: str, index: int):
        """
        Returns a WebElement using the desired selector.
        Can't be used outside the BasePage class.
        """

        by = None
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'id' in selector.keys():
            by = By.ID
            selector = selector['id']
        elif 'link_text' in selector.keys():
            by = By.LINK_TEXT
            selector = selector['link_text']
        elif 'class' in selector.keys():
            by = By.CLASS_NAME
            selector = selector['class']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        elif 'tag' in selector.keys():
            by = By.TAG_NAME
            selector = selector['tag']

        elements = self.driver.find_elements(by, selector)
        if not elements:
            return None
        else:
            return elements[index]

    def _wait_for_element_visibility(self, selector: str, index=0):
        """
        Waits for the WebElement defined in __element method to become visible.
        Can be used in inherited Page Objects.
        """

        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of
                                                       (self.__element(selector, index)))

    def _wait_for_element_visibility_2(self, selector: str, index=0):
        self.driver.switchTo().frame("doc-preview-frame")
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of
                                                       (self.__element(selector, index)))

    def _click(self, selector: str, index=0):
        """
        Clicks on the WebElement defined in __element method, when the element becomes visible.
        Waits 3 seconds after the click for the next page or element to load.
        Can be used in inherited Page Objects.
        """

        self._wait_for_element_visibility(selector, index)
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()
        time.sleep(1)

    def _check_if_element_is_visible(self, selector: str, index=0):
        element = self.__element(selector, index)
        try:
            self.__element(selector, index)
        except NoSuchElementException:
            return False
        is_displayed = element.is_displayed()
        return is_displayed

    def _scroll_to(self, selector: str, index=0):
        """
        Scrolls to the WebElement defined in __element method.
        Can be used in inherited Page Objects.
        """

        self.driver.execute_script("arguments[0].scrollIntoView();", self.__element(selector, index))

    def _hover(self, selector: str, index=0):
        """
        Hovers on the WebElement defined in __element method.
        Waits 3 seconds after hovering.
        Can be used in inherited Page Objects.
        """

        ActionChains(self.driver).move_to_element(self.__element(selector, index)).perform()

    def _input_text(self, text: str, selector: str, index=0):
        """
        Inputs required text to the WebElement defined in __element method.
        Can be used in inherited Page Objects.
        """

        self._click(selector, index)
        # self._scroll_to(selector, index)
        self._wait_for_element_visibility(selector, index)
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(text)

    def _get_element_text(self, selector: str, index=0):
        """
        Returns a WebElement's text.
        Can be used in inherited Page Objects.
        """
        self._scroll_to(selector, index)
        self._wait_for_element_visibility(selector, index)
        text = self.__element(selector, index).text
        return text