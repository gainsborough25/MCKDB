# Model Class

class VWSearchNameAndKits():
    def __init__(self, keycapSetID: str, manu: str, keycapName: str, setColors:str, kitID: int, kitName: str, legendChar: str, sublegendChar: str, numberOfKeys: int, tsangan: int, iso: int):
        self._keycapSetID = keycapSetID
        self._manu = manu
        self._setColors = setColors
        self._keycapName = keycapName
        self._kitID = kitID
        self._kitName = kitName
        self._legendChar = legendChar
        self._sublegendChar = sublegendChar
        self._numberOfKeys = numberOfKeys
        self._tsangan = tsangan
        self._iso = iso

    @property
    def keycapSetID(self):
        return self._keycapSetID

    @property
    def manu(self):
        return self._manu

    @property
    def setColors(self):
        return self._setColors

    @property
    def keycapName(self):
        return self._keycapName

    @property
    def kitID(self):
        return self._kitID

    @property
    def kitName(self):
        return self._kitName

    @property
    def legendChar(self):
        return self._legendChar

    @property
    def sublegendChar(self):
        return self._sublegendChar

    @property
    def numberOfKeys(self):
        return self._numberOfKeys

    @property
    def tsangan(self):
        return self._tsangan

    @property
    def iso(self):
        return self._iso
