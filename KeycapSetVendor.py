# Model Class

class keycapSetVendor():
    def __init__(self, id: int, name: str, price: float):
        self._id = id
        self._keycapSetID = name
        self._vendorID = price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id    

    @property
    def vendorID(self):
        return self._vendorID

    @vendorID.setter
    def vendorID(self, vendorID):
        self._vendorID = vendorID

    @property
    def keycapSetID(self):
        return self._keycapSetID

    @keycapSetID.setter
    def keycapSetID(self, keycapSetID):
        self._keycapSetID = keycapSetID