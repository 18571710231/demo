import unittest

from Web.libs.CommonFunction import CommonFunction
from Web.libs.BusinessFunction import BusinessFunction


class TestTradeTest(unittest.TestCase):
    def setUp(self):
        self.obj = BusinessFunction()
        self.obj_r = CommonFunction()
        self.obj.open_url()

    def tearDown(self):
        self.obj.close_browser()

    def test_trade_001(self):
        self.obj.trade("USDT","CRO")
        text=self.obj.getTextByCss(".pair-toggle")
        print(f"text: {text}")
        self.assertEqual(text,"CRO/USDT")
        #b=self.obj_r.readExcel("trade.xlsx")


if __name__ == '__main__':
    unittest.main(verbosity=2)