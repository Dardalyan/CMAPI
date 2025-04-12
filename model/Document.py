from datetime import date


class BaseDocument:

    def __init__(self, code):
        self.__countryCode = "TR"

        if code == 'CES' or code == 'RHS':
            self.__code = code
        else:
            code = list(filter(lambda x: x[1] == code, self.docCodeList()["iso"]))
            self.__code = code[0][1] if len(code) != 0 else None

        if self.__code is None: raise Exception('The given document code is not acceptable !')

    def getCountryCode(self):
        return self.__countryCode

    def getCode(self):
        return self.__code

    @classmethod
    def docCodeList(cls):
        return {
            "iso": [
                ("9001", "QMS"),
                ("14001", "EMS"),
                ("22000", "FSS"),
                ("45001", "OHS"),
                ("13485", "MDC"),
                ("22301", "BCM"),
                ("20000-1", "BTS"),
                ("27001", "ISS"),
            ],
            "ce": "CES",
            "RoHS": "RHS"
        }


class Document(BaseDocument):

    def __init__(self, code, firmName, startDate: date, endDate: date, docNum):
        super().__init__(code)

        self.__firmName = firmName

        self.__startDate = startDate
        self.__endDate = endDate
        self.__isActive = True if date.today() < self.__endDate else False

        self.__docNum = f"0{docNum}" if docNum < 10 else str(docNum)

        mstr = f"0{self.__startDate.month}" if self.__startDate.month < 10 else f"{self.__startDate.month}"
        self.__docCode = (
            f"{self.getCountryCode()}-"
            f"{self.getCode()}"
            f"{str(self.__startDate.year)[2]}"
            f"{str(self.__startDate.year)[3]}"
            f"{mstr}"
            f"{str(self.__docNum)}"
        )

    def getFirmName(self): return self.__firmName

    def getDocCode(self): return self.__docCode

    def getDocNum(self): return self.__docNum

    def getIsActive(self): return self.__isActive

    def getStartDate(self): return self.__startDate

    def getEndDate(self): return self.__endDate

    def getDict(self):
        return {
            "FirmName": self.getFirmName(),
            "CountryCode": self.getCountryCode(),
            "Code": self.getCode(),
            "DocNum": self.getDocNum(),
            "IsActive": self.getIsActive(),
            "StartDate": str(self.getStartDate()),
            "EndDate": str(self.getEndDate()),
            "DocCode": self.getDocCode(),
        }
