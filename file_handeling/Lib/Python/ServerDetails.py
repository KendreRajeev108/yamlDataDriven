import time
import configparser
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
# from BasePage import BasePage
from robot.api import logger
from logging import Logger as log
from Lib.Python.webWaits import customwebDriverwait


class ServerDetailsPage(customwebDriverwait):

    def __init__(self, webDriver) -> None:
        self.webDriver = webDriver
        logger.info('In Common Utilities constructor')
        # pass

    def wait_for_page_loaded(self):
        try:
            WebDriverWait(self.webDriver, 30).until(
                lambda d: d.execute_script('return document.readyState') == 'complete')
        except TimeoutException:
            logger.error("Timeout waiting for page to load")
            # logger.
    def isElementDisplayed(self, xpath):
        try:
            elementPresense = super().WaitFor_PresenseOf_Element_Located(xpath)
            elementVisible = super().WaitFor_VisibilityOf_Element_Located(xpath)
            if(elementPresense):
                if(elementVisible):
                    return self.webDriver.find_element(By.XPATH, xpath).is_displayed()
        except Exception as error:
            raise error