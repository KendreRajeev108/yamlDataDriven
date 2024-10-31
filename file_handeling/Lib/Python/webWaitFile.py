from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os

from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class WebDriverwait:
    def __init__(self, webDriver):
        #( "this is correct")
        self.webDriver = webDriver
        self.__wait=10


    @property
    def customWait(self):
         ##print("getter method called")
         return self.__wait
       
     # a setter function
    @customWait.setter
    def customWait(self, wait=None):
         ##print("custom wait is set to=",wait)
         if(wait!=None):
            self.__wait = wait
         else:
            wait=10
            self.__wait=wait
            
    def WaitFor_title_contains(self, text_):
        try:
        # page_title=self.webDriver.title
            return WebDriverWait(self.webDriver, self.customWait).until(EC.title_contains(text_))
        except Exception as error:
            raise error
    '''An expectation for checking the title of a page. title is the expected title, 
    which must be an exact match returns True if the title matches, false otherwise.'''

    def WaitFor_title_is(self, text_):
        try:
            # page_title=self.webDriver.title
            return WebDriverWait(self.webDriver, self.customWait).until(EC.title_is(text_))
        except Exception as error:
            raise error
    '''An expectation for checking the current url. url is the expected url, 
    which must not be an exact match returns True if the url is different, false otherwise.'''




    def select_by_value(self, value: str) -> None:
        """Select all options that have a value matching the argument. That is,
        when given "foo" this would select an option like:

        <option value="foo">Bar</option>

        :Args:
         - value - The value to match against

        throws NoSuchElementException If there is no option with specified value in SELECT
        """
        css = f"option[value ={self._escape_string(value)}]"
        opts = self._el.find_elements(By.CSS_SELECTOR, css)
        matched = False
        for opt in opts:
            self._set_selected(opt)
            if not self.is_multiple:
                return
            matched = True
        if not matched:
            raise NoSuchElementException(f"Cannot locate option with value: {value}")

    def select_by_index(self, index: int) -> None:
        """Select the option at the given index. This is done by examining the
        "index" attribute of an element, and not merely by counting.

        :Args:
         - index - The option at this index will be selected

        throws NoSuchElementException If there is no option with specified index in SELECT
        """
        match = str(index)
        for opt in self.options:
            if opt.get_attribute("index") == match:
                self._set_selected(opt)
                return
        raise NoSuchElementException(f"Could not locate element with index {index}")

    def select_by_visible_text(self, text: str) -> None:
        """Select all options that display text matching the argument. That is,
        when given "Bar" this would select an option like:

         <option value="foo">Bar</option>

        :Args:
         - text - The visible text to match against

         throws NoSuchElementException If there is no option with specified text in SELECT
        """
        xpath = f".//option[normalize-space(.) = {self._escape_string(text)}]"
        opts = self._el.find_elements(By.XPATH, xpath)
        matched = False
        for opt in opts:
            self._set_selected(opt)
            if not self.is_multiple:
                return
            matched = True

        if len(opts) == 0 and " " in text:
            sub_string_without_space = self._get_longest_token(text)
            if sub_string_without_space == "":
                candidates = self.options
            else:
                xpath = f".//option[contains(.,{self._escape_string(sub_string_without_space)})]"
                candidates = self._el.find_elements(By.XPATH, xpath)
            for candidate in candidates:
                if text == candidate.text:
                    self._set_selected(candidate)
                    if not self.is_multiple:
                        return
                    matched = True

        if not matched:
            raise NoSuchElementException(f"Could not locate element with visible text: {text}")