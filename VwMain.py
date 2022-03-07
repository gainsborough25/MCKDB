# Model Class
from KeycapSet import KeycapSet

class VwMain():
    def __init__(self, set_instance: KeycapSet, colors: str, numberOfKits: int, regionList: 'str'):
        self._id = set_instance.id
        self._keycapName = set_instance.keycapName
        self._manu = set_instance.manu
        self._material = set_instance.material
        self._printingMethod = set_instance.printingMethod
        self._profile = set_instance.profile
        self._colors = colors
        self._numberOfKits = numberOfKits
        self._regionList =  regionList

    @property
    def id(self): #this allows for just using keycapSet.id, right?
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
    #--------------------> should I also include setters for other classes to update the ID within this thing? Like in junction tables, GBDates, and Kit?

    @property
    def keycapName(self):
        return self._keycapName

    # @keycapName.setter
    # def name(self, keycapName):
    #     self._keycapName = keycapName

    @property
    def manu(self):
        return self._manu

    # @manu.setter
    # def manu(self, manu):
    #     self._manu = manu

    @property
    def material(self):
        return self._material

    # @material.setter
    # def material(self, material):
    #     self._material = material

    @property
    def printingMethod(self):
        return self._printingMethod

    # @material.setter
    # def printingMethod(self, printingMethod):
    #     self._printingMethod = printingMethod

    @property
    def profile(self):
        return self._profile

    # @material.setter
    # def profile(self, profile):
    #     self._profile = profile
    
    @property
    def colors(self):
        return self._colors

    @property
    def numberOfKits(self):
        return self._numberOfKits

    @property
    def regionList(self):
        return self._regionList

    