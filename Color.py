# Model Class

class Color():
    def __init__(self, hex: str, colorFamily: str, shade: str, id = -1,):
        self._id = id
        self._hex = hex
        self._colorFam = colorFamily
        self._shade = shade

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id    

    @property
    def hex(self):
        return self._hex

    @hex.setter
    def name(self, name):
        self._hex = hex

    @property
    def colorFam(self):
        return self._colorFam

    @colorFam.setter
    def colorFam(self, colorFam):
        self._price = colorFam

    @property
    def shade(self):
        return self._shade

    @shade.setter
    def name(self, shade):
        self._shade = shade

