# Model Class

class GBDates():
    def __init__(self, keycapSetID: str, gbStart: str, gbEnd: str):
        self._id = id #still unsure how this is assigned if I used IDENTITY(1, 1)
        self._keycapSetID = keycapSetID
        self._gbStart = gbStart
        self._gbEnd = gbEnd

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id    

    @property
    def keycapSetID(self):
        return self._keycapSetID

    @keycapSetID.setter
    def keycapSetID(self, keycapSetID):
        self._keycapSetID = keycapSetID

    @property
    def gbStart(self):
        return self._gbStart

    @gbStart.setter
    def gbStart(self, gbStart):
        self._gbStart = gbStart

    @property
    def gbEnd(self):
        return self._gbEnd

    @gbEnd.setter
    def gbEnd(self, gbEnd):
        self._gbEnd = gbEnd