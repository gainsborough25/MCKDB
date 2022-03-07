# Model Class

class Kit():
    def __init__(self, kitID: int, keycapSetID: str, kitName: str, legendChar: str, sublegendChar: str, numberOfKeys: int, tsangan: int, iso: int):
        self._kitID = kitID
        self._keycapSetID = keycapSetID
        self._kitName = kitName
        self._legendChar = legendChar
        self._sublegendChar = sublegendChar
        self.numberOfKeys = numberOfKeys
        self._tsangan = tsangan
        self._iso = iso

    @property
    def kitID(self):
        return self._kitID

    @kitID.setter
    def kitID(self, kitID):
        self._kitID = kitID   

    @property
    def keycapSetID(self):
        return self._keycapSetID

    @keycapSetID.setter
    def keycapSetID(self, keycapSetID):
        self._keycapSetID = keycapSetID

    @property
    def kitName(self):
        return self._kitName

    @kitName.setter
    def kitName(self, kitName):
        self._kitName = kitName

    @property
    def legendChar(self):
        return self._legendChar

    @legendChar.setter
    def legendChar(self, legendChar):
        self._legendChar = legendChar  

    @property
    def sublegendChar(self):
        return self._sublegendChar

    @sublegendChar.setter
    def sublegendChar(self, sublegendChar):
        self._sublegendChar = sublegendChar  

    @property
    def numberOfKeys(self):
        return self._numberOfKeys

    @numberOfKeys.setter
    def numberOfKeys(self, numberOfKeys):
        self._numberOfKeys = numberOfKeys

    @property
    def tsangan(self):
        return self._tsangan

    @tsangan.setter
    def tsangan(self, tsangan):
        self._tsangan = tsangan

    @property
    def iso(self):
        return self._iso

    @iso.setter
    def iso(self, iso):
        self._iso = iso