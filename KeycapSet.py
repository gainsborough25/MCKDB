# Model Class

class KeycapSet():
    def __init__(self, keycapName: str, manufacturer: str, material: str, printingMethod: str, profile: str, id ='',):
        if id != '':
            self._id = id
        else:
            if material == 'PBT':
                abb = 'PS'
            elif material == 'ABS':
                abb = 'AH'
            else:
                abb = 'TEST'
            # perform search in DB to see if name exists, if it does, increase int part of key
            self._id = manufacturer[0:1].upper() + keycapName[0:3].upper() + '1' + abb
        self._keycapName = keycapName
        self._manu = manufacturer
        self._material = material
        self._printingMethod = printingMethod
        self._profile = profile

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

    @keycapName.setter
    def name(self, keycapName):
        self._keycapName = keycapName

    @property
    def manu(self):
        return self._manu

    @manu.setter
    def manu(self, manu):
        self._manu = manu

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
    