# Model Class

class KeycapSetColor():
    def __init__(self, keycapSetID: str, colorID: int):
        self._id = id
        self._keycapSetID = keycapSetID
        self._colorID = colorID

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id    

    @property
    def keycapSetID(self):
        return self._keycapSetID

    @keycapSetID.setter # uneeded?  Though I think if i mess up a DB input I might need to change it, so it makes sense to have
    def keycapSetID(self, keycapSetID):
        self._keycapSetID = keycapSetID

    @property
    def colorID(self):
        return self._colorID

    @colorID.setter
    def colorID(self, colorID):
        self._colorID = colorID