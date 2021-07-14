from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Web.libs.CommonFunction import CommonFunction


class Page():
    crypto_url = CommonFunction().getConfig("URL")

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

    def open_url(self):
        self.driver.get(self.crypto_url)
        self.driver.maximize_window()

    def locate_xpath(self,xpath):
        self.driver.find_element_by_xpath(xpath)

    def locate_xpath_and_click(self,xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def explicit_wait(self,locator):
        WebDriverWait(self.driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH,locator)))

    def getTextByCss(self,css):
        text=self.driver.find_element_by_css_selector(css).text
        return text

    def execut_js(self,js):
        self.driver.execute_script(js)

    def close_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    print(Page().open_url())
