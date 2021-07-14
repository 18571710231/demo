import logging

from Web.po.Page import Page


class BusinessFunction(Page):
    def trade(self, price_ccy, base_ccy):
        print("price currency")
        self.explicit_wait(f'//div[contains(@class,"e-tabs__nav-item")][text()="{price_ccy}"]')
        self.locate_xpath_and_click(f'//div[contains(@class,"e-tabs__nav-item")][text()="{price_ccy}"]')
        js = f"""
        document.evaluate('//span[@class="source"][text()="{base_ccy}"]/../../../../..//button[contains(@class,"trade-btn")]',document).iterateNext().click()
        """
        print("开始执行js脚本")
        self.execut_js(js)
        # self.explicit_wait(f'//span[@class="source"][text()="{base_ccy}"]/../../../../..//button[contains(@class,"trade-btn")]')
        # self.locate_xpath_and_click(f'//span[@class="source"][text()="{base_ccy}"]/../../../../..//button[contains(@class,"trade-btn")]')




if __name__ == '__main__':
    print(BusinessFunction().trade("CRO","USD"))