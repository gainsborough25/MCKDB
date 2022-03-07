#uses vwColorSearch w/ VALUE(keycapSetID, Manufacturer, keycapName, Material, PrintingMethod, Profile, NumberOfKits, ColorFamily, ClassesMatchingColor)

from numpy import mat


class ColorSearch():
    def __init__(self, keycapSetID: str, manufacturer: str, keycapName: str, material: str, printingMethod: int, profile: str, numberOfKits: int, colorFam: str, classesMatchingColor: str):
        self._keycapSetID = keycapSetID
        self._manu = manufacturer
        self._keycapName = keycapName
        self._material = material
        self._profile = profile
        self._printingMethod = printingMethod
        self._numberOfKits = numberOfKits
        self._colorFam = colorFam
        self._classesMatchingColor = classesMatchingColor

    @property
    def keycapSetID(self):
        return self._keycapSetID

    @keycapSetID.setter
    def keycapSetID(self, keycapSetID):
        self._keycapSetID = keycapSetID

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

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material

    @property
    def printingMethod(self):
        return self._printingMethod

    @printingMethod.setter
    def printingMethod(self, printingMethod):
        self._printingMethod = printingMethod

    @property
    def profile(self):
        return self._profile

    @profile.setter
    def profile(self, profile):
        self._profile = profile

    @property
    def numberOfKits(self):
        return self._numberOfKits

    @numberOfKits.setter
    def numberOfKits(self, numberOfKits):
        self._numberOfKits = numberOfKits

    @property
    def colorFam(self):
        return self._colorFam

    @colorFam.setter
    def colorFam(self, colorFam):
        self._colorFam = colorFam

    @property
    def classesMatchingColor(self):
        return self._classesMatchingColor

    @classesMatchingColor.setter
    def classesMatchingColor(self, classesMatchingColor):
        self._classesMatchingColor = classesMatchingColor