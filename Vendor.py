# Model Class

class Vendor():
    def __init__(self, vendorName: str, region: str, vendorWebsite):
        self._id = id #IDENTITY (1, 1)
        self._vendorName = vendorName
        self._region = region
        if 'http://www' in vendorWebsite or 'https://www' in vendorWebsite:
            self._vendorWebsite == vendorWebsite
        elif 'www' in vendorWebsite:
            self._vendorWebsite = 'https://' + vendorWebsite
        else:
            self._vendorWebsite = 'https://www.' + vendorWebsite

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id    

    @property
    def vendorName(self):
        return self._vendorName

    @vendorName.setter
    def name(self, vendorName):
        self._vendorName = vendorName

    @property
    def region(self):
        return self._region

    @name.setter
    def region(self, region):
        self._region = region

    @property
    def vendorWebsite(self):
        return self._vendorWebsite

    @vendorWebsite.setter
    def vendorWebsite(self, vendorWebsite):
        self._vendorWebsite = vendorWebsite