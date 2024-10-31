import base64
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from webWaits import customwebDriverwait


class webElements:

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

   

    def get_element_screenshot_as_base64(self, xpath, name: str):
        try:
            element_presence = super().WaitFor_PresenseOf_Element_Located(xpath)
            element_visible = super().WaitFor_VisibilityOf_Element_Located(xpath)
            if element_presence:
                if element_visible:
                    with open(self.__webElement_Screenshot_Location() + "/" + name + ".jpg", "wb") as fh:
                        fh.write(base64.urlsafe_b64decode(element_visible.screenshot_as_base64))
                else:
                    self.__raise_element_not_visible_exception(xpath)
            else:
                self.__raise_element_not_present_exception(xpath)
                # return element.screenshot_as_base64
        except Exception as error:
            raise error

    def get_element_screenshot_as_png(self, xpath, name: str):
        try:
            element_presence = super().WaitFor_PresenseOf_Element_Located(xpath)
            element_visible = super().WaitFor_VisibilityOf_Element_Located(xpath)
            if element_presence:
                if element_visible:
                    result_File = self.__webElement_Screenshot_Location() + "/" + name + ".png"
                    with open(result_File, "wb") as fh:
                        fh.write(element_visible.screenshot_as_png)
                        # Image.open(result_File).save(result_File, 'PNG')
                else:
                    self.__raise_element_not_visible_exception(xpath)
            else:
                self.__raise_element_not_present_exception(xpath)
        except Exception as error:
            raise error

    '''
    shadow_root¶
    Returns a shadow root of the element if there is one or an error. Only works from Chromium 96 onwards. Previous versions of Chromium based browsers will throw an assertion exception.

    Returns:	
    ShadowRoot object or
    NoSuchShadowRoot - if no shadow root was attached to element
    
    '''

    def get_Element_shadow_root(self, xpath):
        try:
            element_presence = super().WaitFor_PresenseOf_Element_Located(xpath)
            # element_visible = super().WaitFor_VisibilityOf_Element_Located(xpath)
            if element_presence:
                # if element_visible:
                return element_presence.shadow_root
            else:
                self.__raise_element_not_present_exception(xpath)
        except Exception as error:
            raise error

    def get_Element_size(self, xpath):
        try:
            element_presence = super().WaitFor_PresenseOf_Element_Located(xpath)
            # element_visible = super().WaitFor_VisibilityOf_Element_Located(xpath)
            if element_presence:
                # if element_visible:
                return element_presence.size
            else:
                self.__raise_element_not_present_exception(xpath)
        except Exception as error:
            raise error

    def get_Element_tag_name(self, xpath):
        try:
            element_presence = super().WaitFor_PresenseOf_Element_Located(xpath)
            # element_visible = super().WaitFor_VisibilityOf_Element_Located(xpath)
            if element_presence:
                # if element_visible:
                return element_presence.tag_name
            else:
                self.__raise_element_not_present_exception(xpath)
        except Exception as error:
            raise error

    def click_by_js(self, xpath):
        try:
            if super().WaitFor_PresenseOf_Element_Located(xpath):
                self.driver.execute_script("arguments[0].click;", self.driver.find_element_by_xpath(xpath))
        except Exception as error:
            raise error

    def get_Element_text(self, xpath):
        try:
            element_presence = super().WaitFor_PresenseOf_Element_Located(xpath)
            # element_visible = super().WaitFor_VisibilityOf_Element_Located(xpath)
            if element_presence:
                # if element_visible:
                return element_presence.text
            else:
                self.__raise_element_not_present_exception(xpath)
        except Exception as error:
            raise error

    def __webElement_Screenshot_Location(self):
        try:
            dir_name = os.getcwd() + "/webElement_Screenshots"
            os.makedirs(dir_name, exist_ok=True)
            return dir_name
        except FileExistsError:
            pass

    def __with_findElement_withAnyLocator(self, locatorType, locator):

        # if locatorType == "XPATH":
        try:
            element = super().WaitFor_PresenseOf_Element_Located_AnyLocatorType(locatorType, locator)

            return element
        except Exception as error:
            return error

    def __raise_element_not_present_exception(self, locator):
        raise Exception("element not present : " + locator)

    def __raise_element_not_visible_exception(self, locator):
        raise Exception("element not visible : " + locator)
