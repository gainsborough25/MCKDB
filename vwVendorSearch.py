
class VwVendorSearch():
    def __init__(self, vendorID, vendorName: str, region: str, vendorWebsite, manu: str, keycapName: str):
        self._vendorID = vendorID
        self._vendorName = vendorName
        self._region = region
        self._vendorWebsite = vendorWebsite
        self._manu = manu
        self._keycapName = keycapName

    @property
    def vendorID(self):
        return self._vendorID
    
    @vendorID.setter
    def vendorID(self, vendorID):
        self._vendorID = vendorID


    @property
    def vendorName(self):
        return self._vendorName

    @vendorName.setter
    def vendorName(self, vendorName):
        self._vendorName = vendorName

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        self._region = region

    @property
    def vendorWebsite(self):
        return self._vendorWebsite

    @vendorWebsite.setter
    def vendorWebsite(self, vendorWebsite):
        self._vendorWebsite = vendorWebsite

    @property
    def manu(self):
        return self._manu

    @manu.setter
    def manu(self, manu):
        self._manu = manu

    @property
    def keycapName(self):
        return self._keycapName

    @keycapName.setter
    def keycapName(self, keycapName):
        self._keycapName = keycapName