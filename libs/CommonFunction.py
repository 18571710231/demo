import os
import sys
import yaml
import pandas as pd


class CommonFunction:
    def readExcel(self, excelName, sheet_name=0):
        path = sys.path[1] + r"\Web\cases\\" + excelName
        dataFrame = pd.read_excel(path, sheet_name=sheet_name)
        li = dataFrame.values.tolist()
        return li

    def getConfig(self, parameter):
        path = sys.path[1] + r"\Web\config.yaml"
        stream = open(path)
        data = yaml.load(stream, Loader=yaml.FullLoader)
        return data.get(parameter)
        stream.close()



if __name__ == '__main__':
    print(sys.path)
    print(CommonFunction().getConfig("URL"))
    print(CommonFunction().readExcel("trade.xlsx"))
